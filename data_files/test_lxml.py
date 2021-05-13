

import re
import warnings

try:
    from bs4.builder import LXMLTreeBuilder, LXMLTreeBuilderForXML
    LXML_PRESENT = True
except ImportError, e:
    LXML_PRESENT = False

from bs4 import (
    BeautifulSoup,
    BeautifulStoneSoup,
    )
from bs4.element import Comment, Doctype, SoupStrainer
from bs4.testing import skipIf
from bs4.tests import test_htmlparser
from bs4.testing import (
    HTMLTreeBuilderSmokeTest,
    XMLTreeBuilderSmokeTest,
    SoupTest,
    skipIf,
)

@skipIf(
    not LXML_PRESENT,
    "lxml seems not to be present, not testing its tree builder.")
class LXMLTreeBuilderSmokeTest(SoupTest, HTMLTreeBuilderSmokeTest):
    

    @property
    def default_builder(self):
        return LXMLTreeBuilder()

    def test_out_of_range_entity(self):
        self.assertSoupEquals(
            "<p>foo&
        self.assertSoupEquals(
            "<p>foo&
        self.assertSoupEquals(
            "<p>foo&

    def test_beautifulstonesoup_is_xml_parser(self):
        
        
        with warnings.catch_warnings(record=False) as w:
            soup = BeautifulStoneSoup("<b />")
            self.assertEqual(u"<b/>", unicode(soup.b))

    def test_real_xhtml_document(self):
        
        markup = b
        soup = self.soup(markup)
        self.assertEqual(
            soup.encode("utf-8").replace(b"\n", b''),
            markup.replace(b'\n', b'').replace(
                b'<?xml version="1.0" encoding="utf-8"?>', b''))


@skipIf(
    not LXML_PRESENT,
    "lxml seems not to be present, not testing its XML tree builder.")
class LXMLXMLTreeBuilderSmokeTest(SoupTest, XMLTreeBuilderSmokeTest):
    

    @property
    def default_builder(self):
        return LXMLTreeBuilderForXML()

