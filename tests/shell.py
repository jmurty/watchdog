# -*- coding: utf-8 -*-

"""
    :module: tests.shell
    :synopsis: Common shell operations for testing.
    :author: Yesudeep Mangalapilly <yesudeep@gmail.com>
"""

import os.path
import tempfile
import shutil
import errno


#def tree(path='.', show_files=False):
#    print(path)
#    padding = ''
#    for root, directories, filenames in os.walk(path):
#        print(padding + os.path.basename(root) + os.path.sep)
#        padding = padding + '   '
#        for filename in filenames:
#            print(padding + filename)


def cd(path):
    os.chdir(path)


def pwd():
    path = os.getcwd()
    print(path)
    return path


def mkdir(path, parents=False):
    """Creates a directory (optionally also creates all the parent directories
    in the path)."""
    if parents:
        try:
            os.makedirs(path)
        except OSError, e:
            if not e.errno == errno.EEXIST:
                raise
    else:
        os.mkdir(path)


def rm(path, recursive=False):
    """Deletes files or directories."""
    if os.path.isdir(path):
        if recursive:
            shutil.rmtree(path)
        #else:
        #    os.rmdir(path)
        else:
            raise OSError("rm: %s: is a directory." % path)
    else:
        os.remove(path)


def touch(path, times=None):
    """Updates the modified timestamp of a file or directory."""
    if os.path.isdir(path):
        os.utime(path, times)
    else:
        with open(path, 'ab'):
            os.utime(path, times)


def truncate(path):
    """Truncates a file."""
    with open(path, 'wb'):
        os.utime(path, None)


def mv(src_path, dest_path):
    """Moves files or directories."""
    shutil.move(src_path, dest_path)


def mkdtemp():
    return tempfile.mkdtemp()


def ls(path='.'):
    return os.listdir(path)
