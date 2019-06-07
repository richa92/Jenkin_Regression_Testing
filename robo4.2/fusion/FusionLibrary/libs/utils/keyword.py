import types


def convert_bool(s):
    if isinstance(s, types.BooleanType):
        return s
    elif isinstance(s, types.StringType) or isinstance(s, types.UnicodeType):
        if s.lower() == 'true':
            return True
        elif s.lower() == 'false':
            return False
    raise Exception('Invalid value for boolean conversion: %s' % s)
