#!/robo4.2/4.2/bin/python

"""Utility for tidying Robot files. Aligns columns to tab stops (multiples of 4 space indents), and aligns columns
within blocks of code (tables or individual test cases or user keywords). Wraps lines longer than 128 characters, if
possible.

The file will be replaced with the formatted version. The original file will be stored with .bak appended to the name.

Note that while this utility does a decent job, it has limited IQ. Ultimately, it is up to the developer to ensure
scripts are formatted for readability

Usage:

  ./robot_tidy.py --help
  ./robot_tidy.py [--dryrun] <filename>

Options:

  <filename> - File to tidy.
  --dryrun   - Don't modify the file, just print what it would look like
"""

import re
import argparse
import shutil

TAB_LENGTH = 4
TAB = ' ' * TAB_LENGTH
MIN_OFFSET = 3  # Minimum number of spaces between columns
# If a column entry is too wide, we don't want to shift the other rows too
# far to align with it
MAX_OFFSET = TAB_LENGTH * 5
MAX_LINE_LENGTH = 128


def _next_tab_stop(position):
    """Calculate the next tab stop that is at least MIN_OFFSET spaces beyond the current position."""
    # First offset by MIN_OFFSET
    tab_stop = position + MIN_OFFSET
    # Advance to next multiple of TAB_LENGTH. Python division rounds down;
    # using negatives makes it round up.
    tab_stop = -(-tab_stop / TAB_LENGTH) * TAB_LENGTH
    return tab_stop


def _pad_array(array):
    """Make all rows in the array the same length by padding them with None.

    That makes it easier to calculate alignment of columns when different rows have different numbers of columns.
    """
    max_length = 0
    for row in array:
        if len(row) > max_length:
            max_length = len(row)
    for row in array:
        while len(row) < max_length:
            row += [None]
    return


def _line_can_wrap(line):
    """Determine whether a line can be wrapped. It would need to have at least three columns."""
    # We can't wrap empty columns, continuation characters (...) or columns
    # containing only '\'
    special_column = re.compile(r'^(|\.\.\.|\\)$')
    wrappable_columns = 0
    for column in line:
        if not special_column.match(column):
            wrappable_columns += 1
    return wrappable_columns >= 3


def _wrap_line(line):
    """Make one line into two by splitting off the last column"""
    wrapped_line = []
    indent_column = re.compile(r'^(|\\)$')
    for column in line:
        if indent_column.match(column):
            wrapped_line += [column]
        else:
            break
    wrapped_line += ['...']
    wrapped_line += [line.pop()]

    return TAB.join(line) + '\n' + TAB.join(wrapped_line)


def _align_columns(tab_stop_array):
    """Align the columns within a code block.

    The input tab_stop_array contains the list of tab stops for each row, padded with None to make rows the same length
    """
    i = 0
    while i < len(tab_stop_array[0]):
        # Start with leftmost column and work right
        # Grab initial tab positions for this column
        column = sorted([row[i] for row in tab_stop_array])
        # To figure out if a given tab position exceeds MAX_OFFSET, we have to get an accurate value for min_tab first.
        # The logic is simplest if we just sort the list.
        min_tab = None
        max_tab = None

        # Figure out the left and rightmost  tabs
        for tab in column:
            if tab is None:
                continue
            if min_tab is None or tab < min_tab:
                min_tab = tab
            if (max_tab is None or tab > max_tab) and tab - \
                    min_tab <= MAX_OFFSET:
                max_tab = tab

        # Recalculate the rest of the tab stops after offsetting one to align
        # with the rest
        for j, row in enumerate(tab_stop_array):
            aligned_row = row[:i]
            original_tab = row[i]
            offset = None if original_tab is None else max_tab - original_tab
            if offset is None:
                # This column is not being used on this row. Leave as None, and
                # don't change remaining columns.
                aligned_row += [None]
                aligned_row += row[i + 1:]
            elif offset < 0:
                # The field to the left was much wider than the other fields in that column. Shift the columns to the
                # right and insert an empty column
                aligned_row += [None]
                aligned_row += [original_tab]
                aligned_row += row[i + 1:]
            else:
                # Align this field with others in the column, and recalculate
                # the remaining columns for this row.
                aligned_row += [original_tab + offset]
                for tab in row[i + 1:]:
                    aligned_row += [None if tab is None else tab + offset]
            tab_stop_array[j] = aligned_row

        _pad_array(tab_stop_array)
        i += 1
    return


def _build_line_from_text_and_tab_stops(text_list, tab_stops):
    """Assemble a line of text from a list of column entries and a list of tab stops.

    Each column after the first is prepended with spaces to align it to the next tab stop.
    For example, ["hello", "world"], [8, None] becomes 'hello   world'
    """
    compiled_text = ''
    i = 0
    for text in text_list:
        compiled_text += text
        while i < len(tab_stops) and tab_stops[i] is None:
            # Skip over columns that are not used to next tab stop
            i += 1
        if i >= len(tab_stops):
            break
        tab = tab_stops[i]
        offset = tab - len(compiled_text)
        if offset < MIN_OFFSET:
            raise RuntimeError(
                "Unexpected tab stop at column {0} before end-of-line at column {1}".format(
                    offset,
                    MIN_OFFSET))
        compiled_text += ' ' * offset
        i += 1
    return compiled_text


def _get_list_of_tab_stops(lines):
    """Calculate the list of tab stops for each line.

    Given a list of lines, where each line is a list of column entries, calculate the list of tab stops
    For example, [['Hello', 'World'], ['Second', 'line', 'here']] becomes [[8, None], [12, 20]]
    """
    tab_stop_list = []
    for line in lines:
        position = 0
        tab_stops = []
        for column in line:
            position += len(column)
            position = _next_tab_stop(position)
            tab_stops += [position]
        tab_stops.pop()  # Don't need tab at end of line
        tab_stop_list += [tab_stops]
    _pad_array(tab_stop_list)
    return tab_stop_list


def _align_code_block(code_block):
    """Align the columns in a block of code."""
    aligned_code_block = code_block
    while True:
        # Split the code block into lines of text. Split lines of text into
        # list of columns.
        column_delimiter = re.compile(r'\s{2,}|\t')
        lines_of_text = aligned_code_block.splitlines()
        lines = []
        for line in lines_of_text:
            columns = column_delimiter.split(line)
            lines += [columns]

        # Calculate tab stops for each column
        tab_stop_list = _get_list_of_tab_stops(lines)
        _align_columns(tab_stop_list)

        # Assemble the lists of columns back into lines of text
        realign = False
        lines_of_aligned_text = []
        for l, line in enumerate(lines):
            aligned_line = _build_line_from_text_and_tab_stops(
                line, tab_stop_list[l])
            if len(aligned_line) > MAX_LINE_LENGTH and _line_can_wrap(line):
                # Line is too long. Wrap it. (Will need to redo alignment.)
                aligned_line = _wrap_line(line)
                realign = True
            lines_of_aligned_text += [aligned_line]
        aligned_code_block = '\n'.join(lines_of_aligned_text)

        if not realign:
            break

    return aligned_code_block


def tidy_robot_file(filename, dryrun=False):
    """The main function of this utility. Formats a Robot file.

    filename - File to tidy.
    dryrun   - Don't modify the file, just print what it would look like
    """
    # Read in file
    with open(filename, 'r') as f:
        robot_file_contents = f.read()

    # Remove trailing spaces from each line
    trailing_spaces = re.compile(r'[ \t]+$', re.MULTILINE)
    robot_file_contents = trailing_spaces.sub('', robot_file_contents)

    # Convert table headers to *** HEADER *** format
    table_headers = re.compile(r'^\*+\s+(\w[\w ]*\w)\s+\*+(.*)$', re.MULTILINE)
    robot_file_contents = table_headers.sub(
        r'*** \1 ***\2', robot_file_contents)

    # Break into code blocks (tables, test cases, or keywords; things
    # separated by one or more blank lines)
    start_of_code_block = re.compile(r'\n{2,}', re.MULTILINE)
    code_blocks = start_of_code_block.split(robot_file_contents)

    # Align all cells to tab marks with at least MIN_SPACES spaces
    aligned_file_contents = []
    for code_block in code_blocks:
        if len(code_block) == 0:
            continue
        aligned_file_contents += [_align_code_block(code_block)]

    robot_file_contents = '\n\n'.join(aligned_file_contents)

    # Put two blank lines between code_blocks
    robot_file_contents = re.sub(r'\n+\*', '\n\n\n*', robot_file_contents)

    # Make sure there is one blank line at the end
    robot_file_contents = re.sub(r'\n*$', '\n\n', robot_file_contents)

    if dryrun:
        print robot_file_contents
    else:
        # First, write the changes to a tmp file
        temp_file = filename + ".tmp"
        with open(temp_file, 'w') as f:
            f.write(robot_file_contents)

        # Second, move the original to backup
        shutil.move(filename, filename + ".bak")

        # Finally, move the formatted file to the original
        shutil.move(temp_file, filename)
    return robot_file_contents


if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dryrun",
        help="Show what tidied file will look like but don't overwrite",
        action="store_true")
    parser.add_argument("filename", help="File to tidy")
    args = parser.parse_args()

    # Tidy the file
    tidy_robot_file(args.filename, dryrun=args.dryrun)
