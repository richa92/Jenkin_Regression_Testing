import string
import random


def __prepare_random_range(range, exclusion):
    chars = list(range)

    if type(exclusion) == list and len(exclusion) > 0:
        for ex in exclusion:
            if ex in chars:
                chars.remove(ex)

    return ''.join(chars)


def random_str(randomlength=8, exclusion=None):
    '''
    @summary             =static= Generate a random string with specified length
    @param randomlength  <int> default(8) the length of the string you want to generate
    @param exclusion     <list> char list that you want to exclude from the result
    @return              <string>
    @author              mingxiang.zhong@hp.com John Zhong
    '''
    chars = __prepare_random_range(string.ascii_letters, exclusion)

    length = len(chars) - 1
    while True:
        strs = ''
        for i in range(randomlength):
            strs += chars[random.Random().randint(0, length)]
        break
    return strs


def random_num(randomlength=8, exclusion=None):
    '''
    @summary             =static= Generate a random number with specified length
    @param randomlength  <int> default(8) the length of the string you want to generate
    @param exclusion     <list> digital char list that you want to exclude from the result
    @return              <string>
    @author              mingxiang.zhong@hp.com John Zhong
    '''
    chars = __prepare_random_range(string.digits, exclusion)

    length = len(chars) - 1
    while True:
        strs = ''
        for i in range(randomlength):
            strs += chars[random.Random().randint(0, length)]
        break
    return strs


def random_punctuation(randomlength=8, exclusion=None):
    '''
    @summary             =static= Generate a random punctuation string with specified length
    @param randomlength  <int> default(8) the length of the string you want to generate
    @param exclusion     <list> punctuation char list that you want to exclude from the result
    @return              <string>
    @author              mingxiang.zhong@hp.com John Zhong
    '''
    chars = __prepare_random_range(string.punctuation, exclusion)

    length = len(chars) - 1
    while True:
        strs = None
        for i in range(randomlength):
            if strs:
                strs += chars[random.Random().randint(0, length)]
            else:
                strs = chars[random.Random().randint(0, length)]
        break
    return strs


def random_str_with_num(randomlength=8, exclusion=None, letter_begin=True):
    '''
    @summary             =static= Generate a random string which include ascii letters and digits with specified length
    @param randomlength  <int> default(8) the length of the string you want to generate
    @param exclusion     <list> char list that you want to exclude from the result
    @param letter_begin  <boolean> default(True) set to True if you want to let the string beginning with ascii_letter
    @return              <string>
    @author              mingxiang.zhong@hp.com John Zhong
    '''
    chars = __prepare_random_range(string.ascii_letters + string.digits, exclusion)

    length = len(chars) - 1
    while True:
        strs = ''
        for i in range(randomlength):
            strs += chars[random.Random().randint(0, length)]
        if letter_begin:
            if strs[0] not in string.ascii_letters:
                continue
        break
    return strs


def random_character(randomlength=8, exclusion=None, letter_begin=True):
    '''
    @summary             =static= Generate a random string which include ascii letters, digits and punctuation with specified length
    @param randomlength  <int> default(8) the length of the string you want to generate
    @param exclusion     <list> char list that you want to exclude from the result
    @param letter_begin  <boolean> default(True) set to True if you want to let the string beginning with ascii_letter
    @return              <string>
    @author              mingxiang.zhong@hp.com John Zhong
    '''
    chars = __prepare_random_range(string.ascii_letters + string.digits + string.punctuation, exclusion)

    length = len(chars) - 1
    while True:
        strs = None
        for i in range(randomlength):
            if strs:
                strs += chars[random.Random().randint(0, length)]
            else:
                strs = chars[random.Random().randint(0, length)]
        if letter_begin:
            if strs[0] not in string.ascii_letters:
                continue
        break
    return strs
