

import copy
import functools
import unittest
from unittest import TestCase
from bs4 import BeautifulSoup
from bs4.element import (
    CharsetMetaAttributeValue,
    Comment,
    ContentMetaAttributeValue,
    Doctype,
    SoupStrainer,
)

from bs4.builder import HTMLParserTreeBuilder
default_builder = HTMLParserTreeBuilder


class SoupTest(unittest.TestCase):

    @property
    def default_builder(self):
        return default_builder()

    def soup(self, markup, **kwargs):
        
        builder = kwargs.pop('builder', self.default_builder)
        return BeautifulSoup(markup, builder=builder, **kwargs)

    def document_for(self, markup):
        
        return self.default_builder.test_fragment_to_document(markup)

    def assertSoupEquals(self, to_parse, compare_parsed_to=None):
        builder = self.default_builder
        obj = BeautifulSoup(to_parse, builder=builder)
        if compare_parsed_to is None:
            compare_parsed_to = to_parse

        self.assertEqual(obj.decode(), self.document_for(compare_parsed_to))


class HTMLTreeBuilderSmokeTest(object):

    

    def assertDoctypeHandled(self, doctype_fragment):
        
        doctype_str, soup = self._document_with_doctype(doctype_fragment)

        
        doctype = soup.contents[0]
        self.assertEqual(doctype.__class__, Doctype)
        self.assertEqual(doctype, doctype_fragment)
        self.assertEqual(str(soup)[:len(doctype_str)], doctype_str)

        
        
        self.assertEqual(soup.p.contents[0], 'foo')

    def _document_with_doctype(self, doctype_fragment):
        
        doctype = '<!DOCTYPE %s>' % doctype_fragment
        markup = doctype + '\n<p>foo</p>'
        soup = self.soup(markup)
        return doctype, soup

    def test_normal_doctypes(self):
        
        self.assertDoctypeHandled("html")
        self.assertDoctypeHandled(
            'html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"')

    def test_public_doctype_with_url(self):
        doctype = 'html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"'
        self.assertDoctypeHandled(doctype)

    def test_system_doctype(self):
        self.assertDoctypeHandled('foo SYSTEM "http://www.example.com/"')

    def test_namespaced_system_doctype(self):
        
        self.assertDoctypeHandled('xsl:stylesheet SYSTEM "htmlent.dtd"')

    def test_namespaced_public_doctype(self):
        
        self.assertDoctypeHandled('xsl:stylesheet PUBLIC "htmlent.dtd"')

    def test_real_xhtml_document(self):
        
        markup = b
        soup = self.soup(markup)
        self.assertEqual(
            soup.encode("utf-8").replace(b"\n", b""),
            markup.replace(b"\n", b""))

    def test_deepcopy(self):
        
        copy.deepcopy(self.default_builder)

    def test_p_tag_is_never_empty_element(self):
        
        soup = self.soup("<p/>")
        self.assertFalse(soup.p.is_empty_element)
        self.assertEqual(str(soup.p), "<p></p>")

    def test_unclosed_tags_get_closed(self):
        
        self.assertSoupEquals("<p>", "<p></p>")
        self.assertSoupEquals("<b>", "<b></b>")

        self.assertSoupEquals("<br>", "<br/>")

    def test_br_is_always_empty_element_tag(self):
        
        soup = self.soup("<br></br>")
        self.assertTrue(soup.br.is_empty_element)
        self.assertEqual(str(soup.br), "<br/>")

    def test_nested_formatting_elements(self):
        self.assertSoupEquals("<em><em></em></em>")

    def test_comment(self):
        
        markup = "<p>foo<!--foobar-->baz</p>"
        self.assertSoupEquals(markup)

        soup = self.soup(markup)
        comment = soup.find(text="foobar")
        self.assertEqual(comment.__class__, Comment)

    def test_preserved_whitespace_in_pre_and_textarea(self):
        
        self.assertSoupEquals("<pre>   </pre>")
        self.assertSoupEquals("<textarea> woo  </textarea>")

    def test_nested_inline_elements(self):
        
        b_tag = "<b>Inside a B tag</b>"
        self.assertSoupEquals(b_tag)

        nested_b_tag = "<p>A <i>nested <b>tag</b></i></p>"
        self.assertSoupEquals(nested_b_tag)

        double_nested_b_tag = "<p>A <a>doubly <i>nested <b>tag</b></i></a></p>"
        self.assertSoupEquals(nested_b_tag)

    def test_nested_block_level_elements(self):
        
        soup = self.soup('<blockquote><p><b>Foo</b></p></blockquote>')
        blockquote = soup.blockquote
        self.assertEqual(blockquote.p.b.string, 'Foo')
        self.assertEqual(blockquote.b.string, 'Foo')

    def test_correctly_nested_tables(self):
        
        markup = ('<table id="1">'
                  '<tr>'
                  "<td>Here's another table:"
                  '<table id="2">'
                  '<tr><td>foo</td></tr>'
                  '</table></td>')

        self.assertSoupEquals(
            markup,
            '<table id="1"><tr><td>Here\'s another table:'
            '<table id="2"><tr><td>foo</td></tr></table>'
            '</td></tr></table>')

        self.assertSoupEquals(
            "<table><thead><tr><td>Foo</td></tr></thead>"
            "<tbody><tr><td>Bar</td></tr></tbody>"
            "<tfoot><tr><td>Baz</td></tr></tfoot></table>")

    def test_deeply_nested_multivalued_attribute(self):
        
        
        
        markup = '<table><div><div class="css"></div></div></table>'
        soup = self.soup(markup)
        self.assertEqual(["css"], soup.div.div['class'])

    def test_angle_brackets_in_attribute_values_are_escaped(self):
        self.assertSoupEquals('<a b="<a>"></a>', '<a b="&lt;a&gt;"></a>')

    def test_entities_in_attributes_converted_to_unicode(self):
        expect = u'<p id="pi\N{LATIN SMALL LETTER N WITH TILDE}ata"></p>'
        self.assertSoupEquals('<p id="pi&
        self.assertSoupEquals('<p id="pi&
        self.assertSoupEquals('<p id="pi&ntilde;ata"></p>', expect)

    def test_entities_in_text_converted_to_unicode(self):
        expect = u'<p>pi\N{LATIN SMALL LETTER N WITH TILDE}ata</p>'
        self.assertSoupEquals("<p>pi&
        self.assertSoupEquals("<p>pi&
        self.assertSoupEquals("<p>pi&ntilde;ata</p>", expect)

    def test_quot_entity_converted_to_quotation_mark(self):
        self.assertSoupEquals("<p>I said &quot;good day!&quot;</p>",
                              '<p>I said "good day!"</p>')

    def test_out_of_range_entity(self):
        expect = u"\N{REPLACEMENT CHARACTER}"
        self.assertSoupEquals("&
        self.assertSoupEquals("&
        self.assertSoupEquals("&

    def test_basic_namespaces(self):
        

        markup = b'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:mathml="http://www.w3.org/1998/Math/MathML" xmlns:svg="http://www.w3.org/2000/svg"><head></head><body><mathml:msqrt>4</mathml:msqrt><b svg:fill="red"></b></body></html>'
        soup = self.soup(markup)
        self.assertEqual(markup, soup.encode())
        html = soup.html
        self.assertEqual('http://www.w3.org/1999/xhtml', soup.html['xmlns'])
        self.assertEqual(
            'http://www.w3.org/1998/Math/MathML', soup.html['xmlns:mathml'])
        self.assertEqual(
            'http://www.w3.org/2000/svg', soup.html['xmlns:svg'])

    def test_multivalued_attribute_value_becomes_list(self):
        markup = b'<a class="foo bar">'
        soup = self.soup(markup)
        self.assertEqual(['foo', 'bar'], soup.a['class'])

    
    
    
    
    
    

    def test_soupstrainer(self):
        
        strainer = SoupStrainer("b")
        soup = self.soup("A <b>bold</b> <meta/> <i>statement</i>",
                         parse_only=strainer)
        self.assertEqual(soup.decode(), "<b>bold</b>")

    def test_single_quote_attribute_values_become_double_quotes(self):
        self.assertSoupEquals("<foo attr='bar'></foo>",
                              '<foo attr="bar"></foo>')

    def test_attribute_values_with_nested_quotes_are_left_alone(self):
        text = 
        self.assertSoupEquals(text)

    def test_attribute_values_with_double_nested_quotes_get_quoted(self):
        text = 
        soup = self.soup(text)
        soup.foo['attr'] = 'Brawls happen at "Bob\'s Bar"'
        self.assertSoupEquals(
            soup.foo.decode(),
            )

    def test_ampersand_in_attribute_value_gets_escaped(self):
        self.assertSoupEquals('<this is="really messed up & stuff"></this>',
                              '<this is="really messed up &amp; stuff"></this>')

        self.assertSoupEquals(
            '<a href="http://example.org?a=1&b=2;3">foo</a>',
            '<a href="http://example.org?a=1&amp;b=2;3">foo</a>')

    def test_escaped_ampersand_in_attribute_value_is_left_alone(self):
        self.assertSoupEquals('<a href="http://example.org?a=1&amp;b=2;3"></a>')

    def test_entities_in_strings_converted_during_parsing(self):
        
        
        text = "<p>&lt;&lt;sacr&eacute;&
        expected = u"<p>&lt;&lt;sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</p>"
        self.assertSoupEquals(text, expected)

    def test_smart_quotes_converted_on_the_way_in(self):
        
        
        quote = b"<p>\x91Foo\x92</p>"
        soup = self.soup(quote)
        self.assertEqual(
            soup.p.string,
            u"\N{LEFT SINGLE QUOTATION MARK}Foo\N{RIGHT SINGLE QUOTATION MARK}")

    def test_non_breaking_spaces_converted_on_the_way_in(self):
        soup = self.soup("<a>&nbsp;&nbsp;</a>")
        self.assertEqual(soup.a.string, u"\N{NO-BREAK SPACE}" * 2)

    def test_entities_converted_on_the_way_out(self):
        text = "<p>&lt;&lt;sacr&eacute;&
        expected = u"<p>&lt;&lt;sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</p>".encode("utf-8")
        soup = self.soup(text)
        self.assertEqual(soup.p.encode("utf-8"), expected)

    def test_real_iso_latin_document(self):
        
        

        
        unicode_html = u'<html><head><meta content="text/html; charset=ISO-Latin-1" http-equiv="Content-type"/></head><body><p>Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!</p></body></html>'

        
        
        iso_latin_html = unicode_html.encode("iso-8859-1")

        
        soup = self.soup(iso_latin_html)
        
        result = soup.encode("utf-8")

        
        
        
        expected = unicode_html.replace("ISO-Latin-1", "utf-8")

        
        expected = expected.encode("utf-8")

        
        self.assertEqual(result, expected)

    def test_real_shift_jis_document(self):
        
        
        shift_jis_html = (
            b'<html><head></head><body><pre>'
            b'\x82\xb1\x82\xea\x82\xcdShift-JIS\x82\xc5\x83R\x81[\x83f'
            b'\x83B\x83\x93\x83O\x82\xb3\x82\xea\x82\xbd\x93\xfa\x96{\x8c'
            b'\xea\x82\xcc\x83t\x83@\x83C\x83\x8b\x82\xc5\x82\xb7\x81B'
            b'</pre></body></html>')
        unicode_html = shift_jis_html.decode("shift-jis")
        soup = self.soup(unicode_html)

        
        
        self.assertEqual(soup.encode("utf-8"), unicode_html.encode("utf-8"))
        self.assertEqual(soup.encode("euc_jp"), unicode_html.encode("euc_jp"))

    def test_real_hebrew_document(self):
        
        
        hebrew_document = b'<html><head><title>Hebrew (ISO 8859-8) in Visual Directionality</title></head><body><h1>Hebrew (ISO 8859-8) in Visual Directionality</h1>\xed\xe5\xec\xf9</body></html>'
        soup = self.soup(
            hebrew_document, from_encoding="iso8859-8")
        self.assertEqual(soup.original_encoding, 'iso8859-8')
        self.assertEqual(
            soup.encode('utf-8'),
            hebrew_document.decode("iso8859-8").encode("utf-8"))

    def test_meta_tag_reflects_current_encoding(self):
        
        
        meta_tag = ('<meta content="text/html; charset=x-sjis" '
                    'http-equiv="Content-type"/>')

        
        shift_jis_html = (
            '<html><head>\n%s\n'
            '<meta http-equiv="Content-language" content="ja"/>'
            '</head><body>Shift-JIS markup goes here.') % meta_tag
        soup = self.soup(shift_jis_html)

        
        parsed_meta = soup.find('meta', {'http-equiv': 'Content-type'})
        content = parsed_meta['content']
        self.assertEqual('text/html; charset=x-sjis', content)

        
        self.assertTrue(isinstance(content, ContentMetaAttributeValue))

        
        
        self.assertEqual('text/html; charset=utf8', content.encode("utf8"))

        
        

    def test_html5_style_meta_tag_reflects_current_encoding(self):
        
        
        meta_tag = ('<meta id="encoding" charset="x-sjis" />')

        
        shift_jis_html = (
            '<html><head>\n%s\n'
            '<meta http-equiv="Content-language" content="ja"/>'
            '</head><body>Shift-JIS markup goes here.') % meta_tag
        soup = self.soup(shift_jis_html)

        
        parsed_meta = soup.find('meta', id="encoding")
        charset = parsed_meta['charset']
        self.assertEqual('x-sjis', charset)

        
        self.assertTrue(isinstance(charset, CharsetMetaAttributeValue))

        
        
        self.assertEqual('utf8', charset.encode("utf8"))

    def test_tag_with_no_attributes_can_have_attributes_added(self):
        data = self.soup("<a>text</a>")
        data.a['foo'] = 'bar'
        self.assertEqual('<a foo="bar">text</a>', data.a.decode())

class XMLTreeBuilderSmokeTest(object):

    def test_docstring_generated(self):
        soup = self.soup("<root/>")
        self.assertEqual(
            soup.encode(), b'<?xml version="1.0" encoding="utf-8"?>\n<root/>')

    def test_real_xhtml_document(self):
        
        markup = b
        soup = self.soup(markup)
        self.assertEqual(
            soup.encode("utf-8"), markup)

    def test_popping_namespaced_tag(self):
        markup = '<rss xmlns:dc="foo"><dc:creator>b</dc:creator><dc:date>2012-07-02T20:33:42Z</dc:date><dc:rights>c</dc:rights><image>d</image></rss>'
        soup = self.soup(markup)
        self.assertEqual(
            unicode(soup.rss), markup)

    def test_docstring_includes_correct_encoding(self):
        soup = self.soup("<root/>")
        self.assertEqual(
            soup.encode("latin1"),
            b'<?xml version="1.0" encoding="latin1"?>\n<root/>')

    def test_large_xml_document(self):
        
        markup = (b'<?xml version="1.0" encoding="utf-8"?>\n<root>'
                  + b'0' * (2**12)
                  + b'</root>')
        soup = self.soup(markup)
        self.assertEqual(soup.encode("utf-8"), markup)


    def test_tags_are_empty_element_if_and_only_if_they_are_empty(self):
        self.assertSoupEquals("<p>", "<p/>")
        self.assertSoupEquals("<p>foo</p>")

    def test_namespaces_are_preserved(self):
        markup = '<root xmlns:a="http://example.com/" xmlns:b="http://example.net/"><a:foo>This tag is in the a namespace</a:foo><b:foo>This tag is in the b namespace</b:foo></root>'
        soup = self.soup(markup)
        root = soup.root
        self.assertEqual("http://example.com/", root['xmlns:a'])
        self.assertEqual("http://example.net/", root['xmlns:b'])

    def test_closing_namespaced_tag(self):
        markup = '<p xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:date>20010504</dc:date></p>'
        soup = self.soup(markup)
        self.assertEqual(unicode(soup.p), markup)

    def test_namespaced_attributes(self):
        markup = '<foo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><bar xsi:schemaLocation="http://www.example.com"/></foo>'
        soup = self.soup(markup)
        self.assertEqual(unicode(soup.foo), markup)

class HTML5TreeBuilderSmokeTest(HTMLTreeBuilderSmokeTest):
    

    def test_real_xhtml_document(self):
        
        
        pass

    def test_html_tags_have_namespace(self):
        markup = "<a>"
        soup = self.soup(markup)
        self.assertEqual("http://www.w3.org/1999/xhtml", soup.a.namespace)

    def test_svg_tags_have_namespace(self):
        markup = '<svg><circle/></svg>'
        soup = self.soup(markup)
        namespace = "http://www.w3.org/2000/svg"
        self.assertEqual(namespace, soup.svg.namespace)
        self.assertEqual(namespace, soup.circle.namespace)


    def test_mathml_tags_have_namespace(self):
        markup = '<math><msqrt>5</msqrt></math>'
        soup = self.soup(markup)
        namespace = 'http://www.w3.org/1998/Math/MathML'
        self.assertEqual(namespace, soup.math.namespace)
        self.assertEqual(namespace, soup.msqrt.namespace)


def skipIf(condition, reason):
   def nothing(test, *args, **kwargs):
       return None

   def decorator(test_item):
       if condition:
           return nothing
       else:
           return test_item

   return decorator
