# -*- coding: utf-8 -*-

from unittest import TestCase
from nose.tools import assert_equals
import houdini
import sys

import sys
if sys.version_info[0] < 3:
    import codecs
    u = lambda x: codecs.unicode_escape_decode(x)[0]
else:
    u = lambda x: x


class EscaperTestCaseMixin(object):
    """Test case mixin for testing methods with an escaper.
    """

    escaper = None
    simple_tests = []

    def test_escapes(self):
        """Escaping returns expected value
        """

        for value, expected in self.simple_tests:
            actual = self.escaper(value)
            self.assertEqual(actual, expected,
                             'escaping %r returned %r rather than the '
                             'expected %r' % (value, actual, expected))
            self.assertEqual(type(actual), type(expected))


class UnescaperTestCaseMixin(object):
    """Test case mixin for testing methods with an unescaper.
    """

    unescaper = None

    def test_unescapes(self):
        """Unescaping returns expected value
        """

        for expected, value in self.simple_tests:
            actual = self.unescaper(value)
            self.assertEqual(actual, expected,
                             'unescaping %r returned %r rather than the '
                             'expected %r' % (value, actual, expected))
            self.assertEqual(type(actual), type(expected))


class HtmlTestCase(UnescaperTestCaseMixin, EscaperTestCaseMixin, TestCase):
    """Test case for :func:`escape_html` and :func:`unescape_html`.
    """

    escaper = staticmethod(houdini.escape_html)
    unescaper = staticmethod(houdini.unescape_html)
    simple_tests = [
        ('hello', 'hello'),
        (u('hello'), u('hello')),
        (u('héllo < hëllo'), u('héllo &lt; hëllo')),
        ('<>&;"', '&lt;&gt;&amp;;&quot;'),
        (u('<>&;"'), u('&lt;&gt;&amp;;&quot;')),
    ]


class XmlTestCase(EscaperTestCaseMixin, TestCase):
    """Test case for :func:`escape_xml`.
    """

    escaper = staticmethod(houdini.escape_xml)
    simple_tests = [
        ('hello', 'hello'),
        (u('hello'), u('hello')),
        (u('héllo < hëllo'), u('héllo &lt; hëllo')),
        ('<>&;"', '&lt;&gt;&amp;;&quot;'),
        (u('<>&;"'), u('&lt;&gt;&amp;;&quot;')),
        ('\x80', '?'),
    ]


class JsTestCase(UnescaperTestCaseMixin, EscaperTestCaseMixin, TestCase):
    """Test case for :func:`escape_js` and :func:`unescape_js`.
    """

    escaper = staticmethod(houdini.escape_js)
    unescaper = staticmethod(houdini.unescape_js)
    simple_tests = [
        ('hello', 'hello'),
        (u('hello'), u('hello')),
        (u('héllo < hëllo'), u('héllo < hëllo')),
        ('\n\t/\\"\'', '\\n\t/\\\\\\"\\\''),
        (u('\n\t"\''), u('\\\\n\\t\\\\"\\\\\'')),
    ]


class UriTestCase(UnescaperTestCaseMixin, EscaperTestCaseMixin, TestCase):
    """Test case for :func:`escape_uri` and :func:`unescape_uri`.
    """

    escaper = staticmethod(houdini.escape_uri)
    unescaper = staticmethod(houdini.unescape_uri)
    simple_tests = [
        ('hello', 'hello'),
        (u('hello'), u('hello')),
        ('http://example.com/uri?param=value',
         'http://example.com/uri?param=value'),
    ]


URL_SAFE = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
URL_SAFE_ORDS = set([i for i, s in enumerate(URL_SAFE) if s])
URL_UNSAFE_ORDS = set(xrange(256)) - URL_SAFE_ORDS
URL_TEST_STRING = ''.join(chr(o) for o in range(1, 256))
URL_TEST_ESCAPED = ''.join(
    '+' if o == 32 else
    '%%%02X' % (o) if o not in URL_SAFE_ORDS else
    chr(o) for o in range(1, 256)
)


class UrlTestCase(UnescaperTestCaseMixin, EscaperTestCaseMixin, TestCase):
    """Test case for :func:`escape_url` and :func:`unescape_url`.
    """

    escaper = staticmethod(houdini.escape_url)
    unescaper = staticmethod(houdini.unescape_url)
    simple_tests = [
        ('hello', 'hello'),
        (u('hello'), u('hello')),
        ('http://example.com/url?param=value',
         'http%3A%2F%2Fexample.com%2Furl%3Fparam%3Dvalue'),
    ]


class UrlSafeTableTestCase(TestCase):
    """Test case for :func:`url_safe_table`.
    """

    def test_escape(self):
        """Escaping with custom safe table returns expected value
        """

        for safe, cases in [
                ('', [
                    ('http://example.com/url?param=value',
                     'http%3A%2F%2Fexample.com%2Furl%3Fparam%3Dvalue'),
                ]),
                ('/', [
                    ('http://example.com/url?param=value',
                     'http%3A//example.com/url%3Fparam%3Dvalue'),
                ]),
        ]:
            safe_table = houdini.url_safe_table(safe)

            for string, expected in cases:
                self.assertEqual(houdini.escape_url_safe_table(string,
                                                               safe_table),
                                 expected)


__all__ = (
    'HtmlTestCase',
    'XmlTestCase',
    'JsTestCase',
    'UriTestCase',
    'UrlTestCase',
)
