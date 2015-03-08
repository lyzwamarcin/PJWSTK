import os.path

__SHORTCUTS_FILE_PATH__ = '..\data\shortcuts.txt'


def read_shortcuts():
    if not os.path.exists(__SHORTCUTS_FILE_PATH__):
        raise IOError('File ' + __SHORTCUTS_FILE_PATH__ + 'not found!')

    return open(__SHORTCUTS_FILE_PATH__, 'r')


def __main__():
    print ''