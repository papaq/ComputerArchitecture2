__author__ = 'solomon'

from time import time


def find_vocabulary_by_field(_list, key, value):
    if not _list:
        return -1
    for i in xrange(len(_list)):
        if _list[i][key] == value:
            return i
    return -1


def update_workers(_list):
    if not _list:
        return
    i = 0
    while i < len(_list):
        if _list[i]["seen"] + 5 < time():
            del _list[i]
        i += 1


def new_client(_list, name):
    index = find_vocabulary_by_field(_list, "name", name)
    if index == -1:
        _list.append({"name": name, "seen": time()})
    else:
        _list[index]["seen"] = time()


def devide_into_substrings(len_a, b, new_len):
    """ new_len is bigger then len_a !!!
    """
    pos = 0
    return_list = []
    if len(b) < new_len:
        return [b]
    while pos + 2 * new_len < len(b):
        return_list.append(b[pos: pos + new_len])
        pos += new_len - len_a + 1
    return_list.append(b[pos: len(b)])
    return return_list


def prepair_tasks(substr_list, substring):
    return [{"number": i, "strings": [substring, substr_list[i]], "done": 0} for i in xrange(len(substr_list))]
