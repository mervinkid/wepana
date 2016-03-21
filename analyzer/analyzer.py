# -*- coding:utf-8 -*-

import os
import re
from urllib import request, error, parse

from . import regex
from . import error as e

# export table
__all__ = [
    'BaseAnalyzer', 'WebPageAnalyzer'
]


class BaseAnalyzer:
    """
    Base Analyzer
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
        """
        constructor
        :param kwargs: url, timeout, charset
        :return:
        """
        url = kwargs.get('url', None)
        timeout = kwargs.get('timeout', None)
        charset = kwargs.get('charset', None)

        # validate timeout
        if isinstance(timeout, int):
            self.timeout = timeout

        # validate charset
        if isinstance(charset, str):
            self.charset = charset

        # validate url and connect
        if isinstance(url, str):
            if self.url_pattern.match(url) is None:
                raise e.InvalidateUrl()
            self.connect(url, timeout=self.timeout)

    def read_text(self, text):
        """
        read content from text
        :param text:
        :return:
        """
        # check type
        if not isinstance(text, str):
            raise TypeError('text must be a str value.')
        self.response_text = text

    def read_file(self, path):
        """
        read content from file
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
        file = open(path, 'r')
        self.response_text = str(file.read())

    def ready(self):
        """
        validate data
        :return: bool
        """
        return self.response_text is not None

    def get_response_text(self):
        """
        export response text
        :return: str
        """
        return self.response_text

    def connect(self, url, **kwargs):
        """
        connect to target url
        :param url: url address
        :param kwargs: timeout, charset
        :return:
        """
        # check arg type
        if not isinstance(url, str):
            raise TypeError('url must be a str value.')

        timeout = kwargs.get('timeout', None)
        if not isinstance(timeout, int):
            raise TypeError('timeout must be a int value.')

        charset = kwargs.get('charset', None)

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
        """
        find content by using pattern
        :param pattern:
        :return:
        """
        return re.findall(pattern, self.response_text)


class WebPageAnalyzer(BaseAnalyzer):
    """
    Web Page Analyzer
    """
    # regex pattern
    title_pattern = re.compile(regex.HTML_TITLE, re.I)
    href_pattern = re.compile(regex.PROPERTY_HREF, re.I)
    image_pattern = re.compile(regex.HTML_IMAGE, re.I)
    src_pattern = re.compile(regex.PROPERTY_SRC, re.I)
    meta_pattern = re.compile(regex.HTML_META, re.I)

    def __init__(self, **kwargs):
        super(WebPageAnalyzer, self).__init__(**kwargs)

    def get_title(self):
        """
        get title
        :return: str
        """
        # validate data
        if not self.ready():
            return ''
        title_tag_search = self.title_pattern.search(self.response_text)
        if title_tag_search is None:
            return ''
        title_tag = str(title_tag_search.group())
        title = title_tag.replace('<title>', '').replace('</title>', '').strip()
        return title

    def get_images(self):
        """
        get images
        :return: list(str())
        """
        # validate data
        if not self.ready():
            return []

        image_tags = self.image_pattern.findall(self.response_text)
        result = []
        for image_tag in image_tags:
            src_properties = self.src_pattern.findall(image_tag)
            if len(src_properties) == 0:
                continue
            src_property = src_properties[0]
            image_url = src_property.replace(r'src=("|\')', '').replace('("|', '').strip()
            if self.url_pattern.match(image_url) is None:
                image_url = '%s%s' % (self.url, image_url)
            result.append(image_url)
        return result

    def get_links(self):
        """
        get links
        :return: list(str())
        """
        # validate data
        if not self.ready():
            return []

        href_list = list(set(self.href_pattern.findall(self.response_text)))
        result = []
        for href in href_list:
            if self.url_pattern.match(href) is None:
                if str(href).startswith('/'):
                    href = '%s%s' % (self.root_url, href)
                else:
                    href = '%s/%s' % (self.url, href)
            result.append(href)
        return result

    def get_metas(self):
        """
        get meta info
        :return: list(str)
        """
        # validate data
        if not self.ready():
            return []

        metas = list(set(self.meta_pattern.findall(self.response_text)))
        return metas

    def get_keywords(self):
        """
        get keywords
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
