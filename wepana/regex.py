# -*- coding: utf-8 -*-

"""
wepana.regex

This module provides regex expression that used for web page content analyzing.
"""

__all__ = [
    'HTML_TITLE',
    'HTML_IMAGE',
    'HTML_A',
    'HTML_META',
    'PROPERTY_SRC',
    'PROPERTY_HREF',
    'URL',
    'ROOT_URL',
    'MAIL'
]

HTML_TITLE = r'<title>[^<]*</title>'
HTML_IMAGE = r'<img(.*?)>'
HTML_A = r'<a[^>]+?href=["\']?([^"\']+)["\']?[^>]*>([^<]+)</a>'
HTML_META = r'<meta(.*?)/>'

PROPERTY_SRC = r'src=["\']?([^"\']+)["\']?'
PROPERTY_HREF = r'href=["\']?([^"\']+)["\']?'

URL = r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?'
ROOT_URL = r'(\w+):\/\/([^\/:]*)(?::(\d+))?'
MAIL = r'[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$'
