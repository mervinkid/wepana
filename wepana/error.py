# -*- coding: utf-8 -*-

"""
wepana.error

This module provides error definitions used by analyzer .
"""

# export table
__all__ = [
    'ConnectionTimeout',
    'FileNotFound',
    'InvalidateUrl'
]


class InvalidateUrl(Exception):
    """invalidate url error
    """

    def __init__(self):
        super(InvalidateUrl, self).__init__('invalidate url address.')


class FileNotFound(Exception):
    """file not found error
    """

    def __init__(self, filename=None):
        if filename is not None and isinstance(filename, str):
            msg = 'specified file [%d] not found.' % filename
        else:
            msg = 'specified file not found.'
        super(FileNotFound, self).__init__(msg)


class ConnectionTimeout(Exception):
    """connection timeout error
    """

    def __init__(self):
        super(ConnectionTimeout, self).__init__('connect timeout.')
