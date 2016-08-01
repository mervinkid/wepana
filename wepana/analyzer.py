# -*- coding: utf-8 -*-

"""
wepana.analyzer

This module provides analyzers
"""

import os
import re
from urllib import request, error, parse

from . import regex
from . import error as e

# export table
__all__ = [
    'BaseAnalyzer',
    'WebPageAnalyzer'
]


class BaseAnalyzer:
    """Base Analyzer
    """
    url = ''
    root_url = ''
    response_text = None
    timeout = 5
    charset = 'utf-8'

    # regex pattern
    url_pattern = re.compile(regex.URL, re.I)
    root_url_pattern = re.compile(regex.ROOT_URL, re.I)

    def __init__(self, **kwargs):
        """constructor
        :param kwargs: url, timeout, charset
        :return:
        """
        url = kwargs.get('url', '')
        timeout = kwargs.get('timeout', 5)
        charset = kwargs.get('charset', 'utf-8')

        # validate timeout
        if isinstance(timeout, int):
            self.timeout = timeout

        # validate charset
        if isinstance(charset, str):
            self.charset = charset

        # validate url and connect
        if isinstance(url, str) and len(url.strip()) != 0:
            if self.url_pattern.match(url) is None:
                raise e.InvalidateUrl()
            self.connect(url, timeout=self.timeout)

    def read_text(self, text):
        """read content from text
        :param text:
        :return:
        """
        # check type
        if not isinstance(text, str):
            raise TypeError('text must be a str value.')
        self.response_text = text

    def read_file(self, path):
        """read content from file
        :param path:
        :return:
        """
        # check type
        if not isinstance(path, str):
            raise TypeError('path must be a str value.')
        # check file
        if not os.path.isfile(path):
            raise FileNotFoundError('file not found.')
        # process file
        content_file = open(path, 'r')
        self.response_text = str(content_file.read())

    def ready(self):
        """validate data
        :return: bool
        """
        return self.response_text is not None

    def reset(self):
        """Reset status
        """
        self.response_text = None

    def get_response_text(self):
        """export response text
        :return: str
        """
        return self.response_text

    def connect(self, url, **kwargs):
        """connect to target url
        :param url: url address
        :param kwargs: timeout, charset
        :return:
        """
        # check arg type
        if not isinstance(url, str):
            raise TypeError('url must be a str value.')

        timeout = kwargs.get('timeout', self.timeout)
        if not isinstance(timeout, int):
            raise TypeError('timeout must be a int value.')

        charset = kwargs.get('charset', self.charset)

        # send http request
        try:
            # prepare url
            url = parse.quote(url, '/:?=&%')
            response = request.urlopen(url, timeout=(self.timeout if timeout is None else timeout))
            self.response_text = bytes(response.read()).decode(self.charset if charset is None else charset)
            self.url = url
            root_url_search = self.root_url_pattern.search(url)
            if root_url_search is not None:
                self.root_url = str(root_url_search.group())
        except error.URLError:
            raise e.ConnectionTimeout()

    def find(self, pattern):
        """find content by using pattern
        :param pattern:
        :return:
        """
        return re.findall(pattern, self.response_text)


class WebPageAnalyzer(BaseAnalyzer):
    """Web Page Analyzer
    """

    def __init__(self, **kwargs):
        super(WebPageAnalyzer, self).__init__(**kwargs)

    def get_title(self):
        """get title
        :return: str
        """
        # validate data
        if not self.ready():
            return ''
        # init regex patterns
        title_pattern = re.compile(regex.HTML_TITLE, re.I)

        title_tag_search = title_pattern.search(self.response_text)
        if title_tag_search is None:
            return ''
        title_tag = str(title_tag_search.group())
        title = title_tag.replace('<title>', '').replace('</title>', '').strip()
        return title

    def get_images(self):
        """get images
        :return: list(str())
        """
        # validate data
        if not self.ready():
            return []

        # init regex patterns
        src_pattern = re.compile(regex.PROPERTY_SRC, re.I)
        url_pattern = re.compile(regex.URL, re.I)
        image_pattern = re.compile(regex.HTML_IMAGE, re.I)

        image_tags = image_pattern.findall(self.response_text)
        result = []
        for image_tag in image_tags:
            src_properties = src_pattern.findall(image_tag)
            if len(src_properties) == 0:
                continue
            src_property = src_properties[0]
            image_url = src_property.replace(r'src=("|\')', '').replace('("|', '').strip(' ')
            if url_pattern.match(image_url) is None:
                if image_url.startswith('//'):
                    image_url = 'http:%s' % image_url
                else:
                    image_url = '%s%s' % (self.url, image_url)
            result.append(image_url)
        return result

    def get_links(self):
        """get links
        :return: list(str())
        """
        # validate data
        if not self.ready():
            return []

        # init regex patterns
        href_pattern = re.compile(regex.PROPERTY_HREF, re.I)

        href_list = list(set(href_pattern.findall(self.response_text)))
        result = []
        # init regex patterns
        url_pattern = re.compile(regex.URL, re.I)
        mail_pattern = re.compile(regex.MAIL, re.I)

        # process
        for href in href_list:
            if url_pattern.match(href) is None and len(mail_pattern.findall(href)) == 0:
                if str(href).startswith('/'):
                    href = '%s%s' % (self.root_url, href)
                else:
                    href = '%s/%s' % (self.url, href)
            result.append(href)
        return result

    def get_metas(self):
        """get meta info
        :return: list(str)
        """
        # validate data
        if not self.ready():
            return []

        # init regex patterns
        meta_pattern = re.compile(regex.HTML_META, re.I)

        # process
        metas = list(set(meta_pattern.findall(self.response_text)))
        return metas

    def get_keywords(self):
        """get keywords
        :return:
        """
        metas = self.get_metas()
        keywords = ''
        for meta in metas:
            if re.search(r'name="keywords"', meta) is None:
                continue
            keyword_contents = re.findall(r'content="(.*?)"', meta)
            if len(keyword_contents) == 0:
                continue
            keywords = keyword_contents[0]
            break
        return keywords.split(',')
