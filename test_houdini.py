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


class BaseTestCase(TestCase):
    """Base test case.
    """

    escaper = None
    simple_tests = []

    def test_escapes(self):
        """Escaping returns expected value
        """

        for value, expected in self.simple_tests:
            actual = self.escaper(value)
            self.assertEqual(actual, expected)
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
            self.assertEqual(actual, expected)
            self.assertEqual(type(actual), type(expected))


class HtmlTestCase(UnescaperTestCaseMixin, BaseTestCase):
    """Test case for :func:`escape_html` and :func:`unescape_html`.
    """

    escaper = houdini.escape_html
    unescaper = houdini.unescape_html
    simple_tests = [
        ('hello', 'hello'),
        (u('hello'), u('hello')),
        (u('héllo < hëllo'), u('héllo &lt; hëllo')),
        ('<>&;"', '&lt;&gt;&amp;;&quot;'),
        (u('<>&;"'), u('&lt;&gt;&amp;;&quot;')),
    ]


__all__ = (
    'HtmlTestCase',
)
