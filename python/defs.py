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
    for i in xrange(len(_list)):
        if _list[i]["seen"] + 4 < time():
            del _list[i]


