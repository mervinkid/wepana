# _*_ coding=utf-8 _*_

__all__ = [
    'HTML_TITLE', 'HTML_IMAGE', 'HTML_A', 'PROPERTY_SRC', 'URL'
]

HTML_TITLE = r'<title>[^<]*</title>'
HTML_IMAGE = r'<img(.*?)>'
HTML_A = r'<a[^>]+?href=["\']?([^"\']+)["\']?[^>]*>([^<]+)</a>'
HTML_META = r'<meta(.*?)/>'

PROPERTY_SRC = r'src=["\']?([^"\']+)["\']?'
PROPERTY_HREF = r'href=["\']?([^"\']+)["\']?'

URL = r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?'
ROOT_URL = r'(\w+):\/\/([^\/:]*)(?::(\d+))?'
