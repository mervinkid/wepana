# -*- coding: utf-8 -*-

"""
wepana.error

This module provides error definitions used by analyzer .
"""

__all__ = [
    'ConnectionTimeout',
    'InvalidateUrl'
]


class InvalidateUrl(Exception):
    """invalidate url error
    """

    def __init__(self):
        super(InvalidateUrl, self).__init__('invalidate url address')


class ConnectionTimeout(Exception):
    """connection timeout error
    """

    def __init__(self):
        super(ConnectionTimeout, self).__init__('connect timeout')
