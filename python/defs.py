__author__ = 'solomon'

from time import time


def find_vocabulary_by_field(_list, key, value):
    """
    Finds index of the vocabulary in a list,
    in which a key contains value
    :param _list: list with vocabularies
    :param key: key in vocabulary
    :param value: sought-for value
    :return: index
    """
    if not _list:
        return -1
    for i in xrange(len(_list)):
        if _list[i][key] == value:
            return i
    return -1


def update_workers(_list):
    """
    Updates worker list, deleting
    killed or slept workers
    :param _list: list with workers
    :return: nothing
    """
    if not _list:
        return
    i = 0
    while i < len(_list):
        if _list[i]["seen"] + 5 < time():
            del _list[i]
        i += 1


def new_client(_list, name):
    """
    Adds new client name or just
    updates its last-seen time
    :param _list: list with clients' names
    :param name: new name
    :return: nothing
    """
    index = find_vocabulary_by_field(_list, "name", name)
    if index == -1:
        _list.append({"name": name, "seen": time()})
    else:
        _list[index]["seen"] = time()


def devide_into_substrings(len_a, b, new_len):
    """
    Divides b into substings according to length new_len

    !!! new_len must be bigger then len_a and less than len(b) !!!

    :param len_a: length of sought-for string
    :param b: string b
    :param new_len: new substring length
    :return: list of substrings
    """
    pos = 0
    return_list = []
    if len(b) < new_len or new_len < len_a:
        return [b]
    while pos + 2 * new_len < len(b):
        return_list.append(b[pos: pos + new_len])
        pos += new_len - len_a + 1
    return_list.append(b[pos: len(b)])
    return return_list


def prepair_tasks(substr_list, substring):
    """
    Makes list of subtasks
    :param substr_list: list of substrings
    :param substring: sought-for substring
    :return: list of subtasks
    """
    return [{"number": i, "strings": [substring, substr_list[i]], "done": 0} for i in xrange(len(substr_list))]
