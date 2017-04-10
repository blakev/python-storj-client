#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~
# >>
#   blake, python-storj-client
# <<

import os
import logging
import subprocess
from contextlib import contextmanager

logger = logging.getLogger(__name__)

BINARY_NAME = 'storj'


class StorjClientError(Exception):
    """ Base exception for errors raised via this library. """


class StorjBinaryError(StorjClientError):
    """ Exceptions raised during the processing/handling of output from the Storj cli binary. """


def _storj_installed(abspath=None):
    if not abspath:
        # use a relative binary name, hopefully in PATH
        path = BINARY_NAME
    else:
        if not os.path.exists(abspath):
            return False
        path = abspath
    # check the exit code was 0
    try:
        subprocess.check_call(path, shell=True)
    except subprocess.CalledProcessError as e:
        return False
    return True


class Storj(object):
    def __init__(self):
        pass


class StorjUser(object):
    def __init__(self):
        self._buckets = None

    @property
    def buckets(self):
        pass

    @contextmanager
    def bucket(self, bucket_id):
        pass

    def add_bucket(self):
        pass

    def remove_bucket(self):
        pass

    def update_bucket(self):
        pass


class Bucket(object):
    def __init__(self, bucket_id):
        pass

    def get_info(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def __del__(self):
        self.delete()


if __name__ == '__main__':
    print(_storj_installed())
    get_info()
