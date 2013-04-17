# -*- coding: utf-8 -*-

from nose.tools import assert_equals

import houdini


def test_escapes_stuff_if_necessary():
    string = u"<>&;\""
    escaped = houdini.escape_html(string)
    assert_equals(escaped, u'&lt;&gt;&amp;;&quot;')

def test_doesnt_escape_stuff_if_it_doesnt_need_to():
    string = u'hello'
    escaped = houdini.escape_html(string)
    assert string is escaped

def test_output_preserves_unicodeness():
    string = u'héllo < hëllo'
    escaped = houdini.escape_html(string)
    assert_equals(escaped, u'héllo &lt; hëllo')
