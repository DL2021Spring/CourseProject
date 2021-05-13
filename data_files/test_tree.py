


import copy
import pickle
import re
import warnings
from bs4 import BeautifulSoup
from bs4.builder import (
    builder_registry,
    HTMLParserTreeBuilder,
)
from bs4.element import (
    CData,
    Doctype,
    NavigableString,
    SoupStrainer,
    Tag,
)
from bs4.testing import (
    SoupTest,
    skipIf,
)

XML_BUILDER_PRESENT = (builder_registry.lookup("xml") is not None)
LXML_PRESENT = (builder_registry.lookup("lxml") is not None)

class TreeTest(SoupTest):

    def assertSelects(self, tags, should_match):
        
        self.assertEqual([tag.string for tag in tags], should_match)

    def assertSelectsIDs(self, tags, should_match):
        
        self.assertEqual([tag['id'] for tag in tags], should_match)


class TestFind(TreeTest):
    

    def test_find_tag(self):
        soup = self.soup("<a>1</a><b>2</b><a>3</a><b>4</b>")
        self.assertEqual(soup.find("b").string, "2")

    def test_unicode_text_find(self):
        soup = self.soup(u'<h1>Räksmörgås</h1>')
        self.assertEqual(soup.find(text=u'Räksmörgås'), u'Räksmörgås')

class TestFindAll(TreeTest):
    

    def test_find_all_text_nodes(self):
        
        soup = self.soup("<html>Foo<b>bar</b>\xbb</html>")
        
        self.assertEqual(soup.find_all(text="bar"), [u"bar"])
        
        self.assertEqual(
            soup.find_all(text=["Foo", "bar"]), [u"Foo", u"bar"])
        
        self.assertEqual(soup.find_all(text=re.compile('.*')),
                         [u"Foo", u"bar", u'\xbb'])
        
        self.assertEqual(soup.find_all(text=True),
                         [u"Foo", u"bar", u'\xbb'])

    def test_find_all_limit(self):
        
        soup = self.soup("<a>1</a><a>2</a><a>3</a><a>4</a><a>5</a>")
        self.assertSelects(soup.find_all('a', limit=3), ["1", "2", "3"])
        self.assertSelects(soup.find_all('a', limit=1), ["1"])
        self.assertSelects(
            soup.find_all('a', limit=10), ["1", "2", "3", "4", "5"])

        
        self.assertSelects(
            soup.find_all('a', limit=0), ["1", "2", "3", "4", "5"])

    def test_calling_a_tag_is_calling_findall(self):
        soup = self.soup("<a>1</a><b>2<a id='foo'>3</a></b>")
        self.assertSelects(soup('a', limit=1), ["1"])
        self.assertSelects(soup.b(id="foo"), ["3"])

    def test_find_all_with_self_referential_data_structure_does_not_cause_infinite_recursion(self):
        soup = self.soup("<a></a>")
        
        l = []
        l.append(l)

        
        
        self.assertEqual([], soup.find_all(l))

class TestFindAllBasicNamespaces(TreeTest):

    def test_find_by_namespaced_name(self):
        soup = self.soup('<mathml:msqrt>4</mathml:msqrt><a svg:fill="red">')
        self.assertEqual("4", soup.find("mathml:msqrt").string)
        self.assertEqual("a", soup.find(attrs= { "svg:fill" : "red" }).name)


class TestFindAllByName(TreeTest):
    

    def setUp(self):
        super(TreeTest, self).setUp()
        self.tree =  self.soup()

    def test_find_all_by_tag_name(self):
        
        self.assertSelects(
            self.tree.find_all('a'), ['First tag.', 'Nested tag.'])

    def test_find_all_by_name_and_text(self):
        self.assertSelects(
            self.tree.find_all('a', text='First tag.'), ['First tag.'])

        self.assertSelects(
            self.tree.find_all('a', text=True), ['First tag.', 'Nested tag.'])

        self.assertSelects(
            self.tree.find_all('a', text=re.compile("tag")),
            ['First tag.', 'Nested tag.'])


    def test_find_all_on_non_root_element(self):
        
        self.assertSelects(self.tree.c.find_all('a'), ['Nested tag.'])

    def test_calling_element_invokes_find_all(self):
        self.assertSelects(self.tree('a'), ['First tag.', 'Nested tag.'])

    def test_find_all_by_tag_strainer(self):
        self.assertSelects(
            self.tree.find_all(SoupStrainer('a')),
            ['First tag.', 'Nested tag.'])

    def test_find_all_by_tag_names(self):
        self.assertSelects(
            self.tree.find_all(['a', 'b']),
            ['First tag.', 'Second tag.', 'Nested tag.'])

    def test_find_all_by_tag_dict(self):
        self.assertSelects(
            self.tree.find_all({'a' : True, 'b' : True}),
            ['First tag.', 'Second tag.', 'Nested tag.'])

    def test_find_all_by_tag_re(self):
        self.assertSelects(
            self.tree.find_all(re.compile('^[ab]$')),
            ['First tag.', 'Second tag.', 'Nested tag.'])

    def test_find_all_with_tags_matching_method(self):
        
        
        def id_matches_name(tag):
            return tag.name == tag.get('id')

        tree = self.soup()

        self.assertSelects(
            tree.find_all(id_matches_name), ["Match 1.", "Match 2."])


class TestFindAllByAttribute(TreeTest):

    def test_find_all_by_attribute_name(self):
        
        
        tree = self.soup()
        self.assertSelects(tree.find_all(id='first'),
                           ["Matching a.", "Matching b."])

    def test_find_all_by_utf8_attribute_value(self):
        peace = u"םולש".encode("utf8")
        data = u'<a title="םולש"></a>'.encode("utf8")
        soup = self.soup(data)
        self.assertEqual([soup.a], soup.find_all(title=peace))
        self.assertEqual([soup.a], soup.find_all(title=peace.decode("utf8")))
        self.assertEqual([soup.a], soup.find_all(title=[peace, "something else"]))

    def test_find_all_by_attribute_dict(self):
        
        
        
        tree = self.soup()

        
        self.assertSelects(tree.find_all(name='name1'),
                           ["A tag called 'name1'."])
        
        self.assertSelects(tree.find_all(attrs={'name' : 'name1'}),
                           ["Name match."])

        self.assertSelects(tree.find_all(attrs={'class' : 'class2'}),
                           ["Class match."])

    def test_find_all_by_class(self):
        tree = self.soup()

        
        
        self.assertSelects(tree.find_all('a', class_='1'), ['Class 1.'])
        self.assertSelects(tree.find_all('c', class_='3'), ['Class 3 and 4.'])
        self.assertSelects(tree.find_all('c', class_='4'), ['Class 3 and 4.'])

        
        self.assertSelects(tree.find_all('a', '1'), ['Class 1.'])
        self.assertSelects(tree.find_all(attrs='1'), ['Class 1.', 'Class 1.'])
        self.assertSelects(tree.find_all('c', '3'), ['Class 3 and 4.'])
        self.assertSelects(tree.find_all('c', '4'), ['Class 3 and 4.'])

    def test_find_by_class_when_multiple_classes_present(self):
        tree = self.soup("<gar class='foo bar'>Found it</gar>")

        f = tree.find_all("gar", class_=re.compile("o"))
        self.assertSelects(f, ["Found it"])

        f = tree.find_all("gar", class_=re.compile("a"))
        self.assertSelects(f, ["Found it"])

        
        
        f = tree.find_all("gar", class_=re.compile("o b"))
        self.assertSelects(f, [])

    def test_find_all_with_non_dictionary_for_attrs_finds_by_class(self):
        soup = self.soup("<a class='bar'>Found it</a>")

        self.assertSelects(soup.find_all("a", re.compile("ba")), ["Found it"])

        def big_attribute_value(value):
            return len(value) > 3

        self.assertSelects(soup.find_all("a", big_attribute_value), [])

        def small_attribute_value(value):
            return len(value) <= 3

        self.assertSelects(
            soup.find_all("a", small_attribute_value), ["Found it"])

    def test_find_all_with_string_for_attrs_finds_multiple_classes(self):
        soup = self.soup('<a class="foo bar"></a><a class="foo"></a>')
        a, a2 = soup.find_all("a")
        self.assertEqual([a, a2], soup.find_all("a", "foo"))
        self.assertEqual([a], soup.find_all("a", "bar"))

        
        
        self.assertEqual([a], soup.find_all("a", class_="foo bar"))
        self.assertEqual([a], soup.find_all("a", "foo bar"))
        self.assertEqual([], soup.find_all("a", "bar foo"))

    def test_find_all_by_attribute_soupstrainer(self):
        tree = self.soup()

        strainer = SoupStrainer(attrs={'id' : 'first'})
        self.assertSelects(tree.find_all(strainer), ['Match.'])

    def test_find_all_with_missing_atribute(self):
        
        
        tree = self.soup()
        self.assertSelects(tree.find_all('a', id=None), ["No ID present."])

    def test_find_all_with_defined_attribute(self):
        
        
        tree = self.soup()
        self.assertSelects(
            tree.find_all(id=True), ["ID present.", "ID is empty."])

    def test_find_all_with_numeric_attribute(self):
        
        tree = self.soup()

        expected = ["Unquoted attribute.", "Quoted attribute."]
        self.assertSelects(tree.find_all(id=1), expected)
        self.assertSelects(tree.find_all(id="1"), expected)

    def test_find_all_with_list_attribute_values(self):
        
        
        tree = self.soup()
        self.assertSelects(tree.find_all(id=["1", "3", "4"]),
                           ["1", "3"])

    def test_find_all_with_regular_expression_attribute_value(self):
        
        
        
        tree = self.soup()

        self.assertSelects(tree.find_all(id=re.compile("^a+$")),
                           ["One a.", "Two as."])

    def test_find_by_name_and_containing_string(self):
        soup = self.soup("<b>foo</b><b>bar</b><a>foo</a>")
        a = soup.a

        self.assertEqual([a], soup.find_all("a", text="foo"))
        self.assertEqual([], soup.find_all("a", text="bar"))
        self.assertEqual([], soup.find_all("a", text="bar"))

    def test_find_by_name_and_containing_string_when_string_is_buried(self):
        soup = self.soup("<a>foo</a><a><b><c>foo</c></b></a>")
        self.assertEqual(soup.find_all("a"), soup.find_all("a", text="foo"))

    def test_find_by_attribute_and_containing_string(self):
        soup = self.soup('<b id="1">foo</b><a id="2">foo</a>')
        a = soup.a

        self.assertEqual([a], soup.find_all(id=2, text="foo"))
        self.assertEqual([], soup.find_all(id=1, text="bar"))




class TestIndex(TreeTest):
    
    def test_index(self):
        tree = self.soup()
        div = tree.div
        for i, element in enumerate(div.contents):
            self.assertEqual(i, div.index(element))
        self.assertRaises(ValueError, tree.index, 1)


class TestParentOperations(TreeTest):
    

    def setUp(self):
        super(TestParentOperations, self).setUp()
        self.tree = self.soup()
        self.start = self.tree.b


    def test_parent(self):
        self.assertEqual(self.start.parent['id'], 'bottom')
        self.assertEqual(self.start.parent.parent['id'], 'middle')
        self.assertEqual(self.start.parent.parent.parent['id'], 'top')

    def test_parent_of_top_tag_is_soup_object(self):
        top_tag = self.tree.contents[0]
        self.assertEqual(top_tag.parent, self.tree)

    def test_soup_object_has_no_parent(self):
        self.assertEqual(None, self.tree.parent)

    def test_find_parents(self):
        self.assertSelectsIDs(
            self.start.find_parents('ul'), ['bottom', 'middle', 'top'])
        self.assertSelectsIDs(
            self.start.find_parents('ul', id="middle"), ['middle'])

    def test_find_parent(self):
        self.assertEqual(self.start.find_parent('ul')['id'], 'bottom')

    def test_parent_of_text_element(self):
        text = self.tree.find(text="Start here")
        self.assertEqual(text.parent.name, 'b')

    def test_text_element_find_parent(self):
        text = self.tree.find(text="Start here")
        self.assertEqual(text.find_parent('ul')['id'], 'bottom')

    def test_parent_generator(self):
        parents = [parent['id'] for parent in self.start.parents
                   if parent is not None and 'id' in parent.attrs]
        self.assertEqual(parents, ['bottom', 'middle', 'top'])


class ProximityTest(TreeTest):

    def setUp(self):
        super(TreeTest, self).setUp()
        self.tree = self.soup(
            '<html id="start"><head></head><body><b id="1">One</b><b id="2">Two</b><b id="3">Three</b></body></html>')


class TestNextOperations(ProximityTest):

    def setUp(self):
        super(TestNextOperations, self).setUp()
        self.start = self.tree.b

    def test_next(self):
        self.assertEqual(self.start.next_element, "One")
        self.assertEqual(self.start.next_element.next_element['id'], "2")

    def test_next_of_last_item_is_none(self):
        last = self.tree.find(text="Three")
        self.assertEqual(last.next_element, None)

    def test_next_of_root_is_none(self):
        
        self.assertEqual(self.tree.next_element, None)

    def test_find_all_next(self):
        self.assertSelects(self.start.find_all_next('b'), ["Two", "Three"])
        self.start.find_all_next(id=3)
        self.assertSelects(self.start.find_all_next(id=3), ["Three"])

    def test_find_next(self):
        self.assertEqual(self.start.find_next('b')['id'], '2')
        self.assertEqual(self.start.find_next(text="Three"), "Three")

    def test_find_next_for_text_element(self):
        text = self.tree.find(text="One")
        self.assertEqual(text.find_next("b").string, "Two")
        self.assertSelects(text.find_all_next("b"), ["Two", "Three"])

    def test_next_generator(self):
        start = self.tree.find(text="Two")
        successors = [node for node in start.next_elements]
        
        tag, contents = successors
        self.assertEqual(tag['id'], '3')
        self.assertEqual(contents, "Three")

class TestPreviousOperations(ProximityTest):

    def setUp(self):
        super(TestPreviousOperations, self).setUp()
        self.end = self.tree.find(text="Three")

    def test_previous(self):
        self.assertEqual(self.end.previous_element['id'], "3")
        self.assertEqual(self.end.previous_element.previous_element, "Two")

    def test_previous_of_first_item_is_none(self):
        first = self.tree.find('html')
        self.assertEqual(first.previous_element, None)

    def test_previous_of_root_is_none(self):
        
        
        
        pass

    def test_find_all_previous(self):
        
        
        
        self.assertSelects(
            self.end.find_all_previous('b'), ["Three", "Two", "One"])
        self.assertSelects(self.end.find_all_previous(id=1), ["One"])

    def test_find_previous(self):
        self.assertEqual(self.end.find_previous('b')['id'], '3')
        self.assertEqual(self.end.find_previous(text="One"), "One")

    def test_find_previous_for_text_element(self):
        text = self.tree.find(text="Three")
        self.assertEqual(text.find_previous("b").string, "Three")
        self.assertSelects(
            text.find_all_previous("b"), ["Three", "Two", "One"])

    def test_previous_generator(self):
        start = self.tree.find(text="One")
        predecessors = [node for node in start.previous_elements]

        
        
        b, body, head, html = predecessors
        self.assertEqual(b['id'], '1')
        self.assertEqual(body.name, "body")
        self.assertEqual(head.name, "head")
        self.assertEqual(html.name, "html")


class SiblingTest(TreeTest):

    def setUp(self):
        super(SiblingTest, self).setUp()
        markup = 
        
        
        markup = re.compile("\n\s*").sub("", markup)
        self.tree = self.soup(markup)


class TestNextSibling(SiblingTest):

    def setUp(self):
        super(TestNextSibling, self).setUp()
        self.start = self.tree.find(id="1")

    def test_next_sibling_of_root_is_none(self):
        self.assertEqual(self.tree.next_sibling, None)

    def test_next_sibling(self):
        self.assertEqual(self.start.next_sibling['id'], '2')
        self.assertEqual(self.start.next_sibling.next_sibling['id'], '3')

        
        self.assertEqual(self.start.next_element['id'], '1.1')

    def test_next_sibling_may_not_exist(self):
        self.assertEqual(self.tree.html.next_sibling, None)

        nested_span = self.tree.find(id="1.1")
        self.assertEqual(nested_span.next_sibling, None)

        last_span = self.tree.find(id="4")
        self.assertEqual(last_span.next_sibling, None)

    def test_find_next_sibling(self):
        self.assertEqual(self.start.find_next_sibling('span')['id'], '2')

    def test_next_siblings(self):
        self.assertSelectsIDs(self.start.find_next_siblings("span"),
                              ['2', '3', '4'])

        self.assertSelectsIDs(self.start.find_next_siblings(id='3'), ['3'])

    def test_next_sibling_for_text_element(self):
        soup = self.soup("Foo<b>bar</b>baz")
        start = soup.find(text="Foo")
        self.assertEqual(start.next_sibling.name, 'b')
        self.assertEqual(start.next_sibling.next_sibling, 'baz')

        self.assertSelects(start.find_next_siblings('b'), ['bar'])
        self.assertEqual(start.find_next_sibling(text="baz"), "baz")
        self.assertEqual(start.find_next_sibling(text="nonesuch"), None)


class TestPreviousSibling(SiblingTest):

    def setUp(self):
        super(TestPreviousSibling, self).setUp()
        self.end = self.tree.find(id="4")

    def test_previous_sibling_of_root_is_none(self):
        self.assertEqual(self.tree.previous_sibling, None)

    def test_previous_sibling(self):
        self.assertEqual(self.end.previous_sibling['id'], '3')
        self.assertEqual(self.end.previous_sibling.previous_sibling['id'], '2')

        
        self.assertEqual(self.end.previous_element['id'], '3.1')

    def test_previous_sibling_may_not_exist(self):
        self.assertEqual(self.tree.html.previous_sibling, None)

        nested_span = self.tree.find(id="1.1")
        self.assertEqual(nested_span.previous_sibling, None)

        first_span = self.tree.find(id="1")
        self.assertEqual(first_span.previous_sibling, None)

    def test_find_previous_sibling(self):
        self.assertEqual(self.end.find_previous_sibling('span')['id'], '3')

    def test_previous_siblings(self):
        self.assertSelectsIDs(self.end.find_previous_siblings("span"),
                              ['3', '2', '1'])

        self.assertSelectsIDs(self.end.find_previous_siblings(id='1'), ['1'])

    def test_previous_sibling_for_text_element(self):
        soup = self.soup("Foo<b>bar</b>baz")
        start = soup.find(text="baz")
        self.assertEqual(start.previous_sibling.name, 'b')
        self.assertEqual(start.previous_sibling.previous_sibling, 'Foo')

        self.assertSelects(start.find_previous_siblings('b'), ['bar'])
        self.assertEqual(start.find_previous_sibling(text="Foo"), "Foo")
        self.assertEqual(start.find_previous_sibling(text="nonesuch"), None)


class TestTagCreation(SoupTest):
    
    def test_new_tag(self):
        soup = self.soup("")
        new_tag = soup.new_tag("foo", bar="baz")
        self.assertTrue(isinstance(new_tag, Tag))
        self.assertEqual("foo", new_tag.name)
        self.assertEqual(dict(bar="baz"), new_tag.attrs)
        self.assertEqual(None, new_tag.parent)

    def test_tag_inherits_self_closing_rules_from_builder(self):
        if XML_BUILDER_PRESENT:
            xml_soup = BeautifulSoup("", "xml")
            xml_br = xml_soup.new_tag("br")
            xml_p = xml_soup.new_tag("p")

            
            
            self.assertEqual(b"<br/>", xml_br.encode())
            self.assertEqual(b"<p/>", xml_p.encode())

        html_soup = BeautifulSoup("", "html")
        html_br = html_soup.new_tag("br")
        html_p = html_soup.new_tag("p")

        
        
        self.assertEqual(b"<br/>", html_br.encode())
        self.assertEqual(b"<p></p>", html_p.encode())

    def test_new_string_creates_navigablestring(self):
        soup = self.soup("")
        s = soup.new_string("foo")
        self.assertEqual("foo", s)
        self.assertTrue(isinstance(s, NavigableString))

class TestTreeModification(SoupTest):

    def test_attribute_modification(self):
        soup = self.soup('<a id="1"></a>')
        soup.a['id'] = 2
        self.assertEqual(soup.decode(), self.document_for('<a id="2"></a>'))
        del(soup.a['id'])
        self.assertEqual(soup.decode(), self.document_for('<a></a>'))
        soup.a['id2'] = 'foo'
        self.assertEqual(soup.decode(), self.document_for('<a id2="foo"></a>'))

    def test_new_tag_creation(self):
        builder = builder_registry.lookup('html')()
        soup = self.soup("<body></body>", builder=builder)
        a = Tag(soup, builder, 'a')
        ol = Tag(soup, builder, 'ol')
        a['href'] = 'http://foo.com/'
        soup.body.insert(0, a)
        soup.body.insert(1, ol)
        self.assertEqual(
            soup.body.encode(),
            b'<body><a href="http://foo.com/"></a><ol></ol></body>')

    def test_append_to_contents_moves_tag(self):
        doc = 
        soup = self.soup(doc)
        second_para = soup.find(id='2')
        bold = soup.b

        
        soup.find(id='2').append(soup.b)

        
        self.assertEqual(bold.parent, second_para)

        self.assertEqual(
            soup.decode(), self.document_for(
                '<p id="1">Don\'t leave me .</p>\n'
                '<p id="2">Don\'t leave!<b>here</b></p>'))

    def test_replace_with_returns_thing_that_was_replaced(self):
        text = "<a></a><b><c></c></b>"
        soup = self.soup(text)
        a = soup.a
        new_a = a.replace_with(soup.c)
        self.assertEqual(a, new_a)

    def test_unwrap_returns_thing_that_was_replaced(self):
        text = "<a><b></b><c></c></a>"
        soup = self.soup(text)
        a = soup.a
        new_a = a.unwrap()
        self.assertEqual(a, new_a)

    def test_replace_tag_with_itself(self):
        text = "<a><b></b><c>Foo<d></d></c></a><a><e></e></a>"
        soup = self.soup(text)
        c = soup.c
        soup.c.replace_with(c)
        self.assertEqual(soup.decode(), self.document_for(text))

    def test_replace_tag_with_its_parent_raises_exception(self):
        text = "<a><b></b></a>"
        soup = self.soup(text)
        self.assertRaises(ValueError, soup.b.replace_with, soup.a)

    def test_insert_tag_into_itself_raises_exception(self):
        text = "<a><b></b></a>"
        soup = self.soup(text)
        self.assertRaises(ValueError, soup.a.insert, 0, soup.a)

    def test_replace_with_maintains_next_element_throughout(self):
        soup = self.soup('<p><a>one</a><b>three</b></p>')
        a = soup.a
        b = a.contents[0]
        
        a.insert(1, "two")

        
        left, right = a.contents
        left.replaceWith('')
        right.replaceWith('')

        
        self.assertEqual("three", soup.b.string)

    def test_replace_final_node(self):
        soup = self.soup("<b>Argh!</b>")
        soup.find(text="Argh!").replace_with("Hooray!")
        new_text = soup.find(text="Hooray!")
        b = soup.b
        self.assertEqual(new_text.previous_element, b)
        self.assertEqual(new_text.parent, b)
        self.assertEqual(new_text.previous_element.next_element, new_text)
        self.assertEqual(new_text.next_element, None)

    def test_consecutive_text_nodes(self):
        
        
        
        soup = self.soup("<a><b>Argh!</b><c></c></a>")
        soup.b.insert(1, "Hooray!")

        self.assertEqual(
            soup.decode(), self.document_for(
                "<a><b>Argh!Hooray!</b><c></c></a>"))

        new_text = soup.find(text="Hooray!")
        self.assertEqual(new_text.previous_element, "Argh!")
        self.assertEqual(new_text.previous_element.next_element, new_text)

        self.assertEqual(new_text.previous_sibling, "Argh!")
        self.assertEqual(new_text.previous_sibling.next_sibling, new_text)

        self.assertEqual(new_text.next_sibling, None)
        self.assertEqual(new_text.next_element, soup.c)

    def test_insert_string(self):
        soup = self.soup("<a></a>")
        soup.a.insert(0, "bar")
        soup.a.insert(0, "foo")
        
        self.assertEqual(["foo", "bar"], soup.a.contents)
        
        self.assertEqual(soup.a.contents[0].next_element, "bar")

    def test_insert_tag(self):
        builder = self.default_builder
        soup = self.soup(
            "<a><b>Find</b><c>lady!</c><d></d></a>", builder=builder)
        magic_tag = Tag(soup, builder, 'magictag')
        magic_tag.insert(0, "the")
        soup.a.insert(1, magic_tag)

        self.assertEqual(
            soup.decode(), self.document_for(
                "<a><b>Find</b><magictag>the</magictag><c>lady!</c><d></d></a>"))

        
        b_tag = soup.b
        self.assertEqual(b_tag.next_sibling, magic_tag)
        self.assertEqual(magic_tag.previous_sibling, b_tag)

        find = b_tag.find(text="Find")
        self.assertEqual(find.next_element, magic_tag)
        self.assertEqual(magic_tag.previous_element, find)

        c_tag = soup.c
        self.assertEqual(magic_tag.next_sibling, c_tag)
        self.assertEqual(c_tag.previous_sibling, magic_tag)

        the = magic_tag.find(text="the")
        self.assertEqual(the.parent, magic_tag)
        self.assertEqual(the.next_element, c_tag)
        self.assertEqual(c_tag.previous_element, the)

    def test_append_child_thats_already_at_the_end(self):
        data = "<a><b></b></a>"
        soup = self.soup(data)
        soup.a.append(soup.b)
        self.assertEqual(data, soup.decode())

    def test_move_tag_to_beginning_of_parent(self):
        data = "<a><b></b><c></c><d></d></a>"
        soup = self.soup(data)
        soup.a.insert(0, soup.d)
        self.assertEqual("<a><d></d><b></b><c></c></a>", soup.decode())

    def test_insert_works_on_empty_element_tag(self):
        
        
        
        
        soup = self.soup("<br/>")
        soup.br.insert(1, "Contents")
        self.assertEqual(str(soup.br), "<br>Contents</br>")

    def test_insert_before(self):
        soup = self.soup("<a>foo</a><b>bar</b>")
        soup.b.insert_before("BAZ")
        soup.a.insert_before("QUUX")
        self.assertEqual(
            soup.decode(), self.document_for("QUUX<a>foo</a>BAZ<b>bar</b>"))

        soup.a.insert_before(soup.b)
        self.assertEqual(
            soup.decode(), self.document_for("QUUX<b>bar</b><a>foo</a>BAZ"))

    def test_insert_after(self):
        soup = self.soup("<a>foo</a><b>bar</b>")
        soup.b.insert_after("BAZ")
        soup.a.insert_after("QUUX")
        self.assertEqual(
            soup.decode(), self.document_for("<a>foo</a>QUUX<b>bar</b>BAZ"))
        soup.b.insert_after(soup.a)
        self.assertEqual(
            soup.decode(), self.document_for("QUUX<b>bar</b><a>foo</a>BAZ"))

    def test_insert_after_raises_exception_if_after_has_no_meaning(self):
        soup = self.soup("")
        tag = soup.new_tag("a")
        string = soup.new_string("")
        self.assertRaises(ValueError, string.insert_after, tag)
        self.assertRaises(NotImplementedError, soup.insert_after, tag)
        self.assertRaises(ValueError, tag.insert_after, tag)

    def test_insert_before_raises_notimplementederror_if_before_has_no_meaning(self):
        soup = self.soup("")
        tag = soup.new_tag("a")
        string = soup.new_string("")
        self.assertRaises(ValueError, string.insert_before, tag)
        self.assertRaises(NotImplementedError, soup.insert_before, tag)
        self.assertRaises(ValueError, tag.insert_before, tag)

    def test_replace_with(self):
        soup = self.soup(
                "<p>There's <b>no</b> business like <b>show</b> business</p>")
        no, show = soup.find_all('b')
        show.replace_with(no)
        self.assertEqual(
            soup.decode(),
            self.document_for(
                "<p>There's  business like <b>no</b> business</p>"))

        self.assertEqual(show.parent, None)
        self.assertEqual(no.parent, soup.p)
        self.assertEqual(no.next_element, "no")
        self.assertEqual(no.next_sibling, " business")

    def test_replace_first_child(self):
        data = "<a><b></b><c></c></a>"
        soup = self.soup(data)
        soup.b.replace_with(soup.c)
        self.assertEqual("<a><c></c></a>", soup.decode())

    def test_replace_last_child(self):
        data = "<a><b></b><c></c></a>"
        soup = self.soup(data)
        soup.c.replace_with(soup.b)
        self.assertEqual("<a><b></b></a>", soup.decode())

    def test_nested_tag_replace_with(self):
        soup = self.soup(
            )

        
        
        remove_tag = soup.b
        move_tag = soup.f
        remove_tag.replace_with(move_tag)

        self.assertEqual(
            soup.decode(), self.document_for(
                "<a>We<f>refuse</f></a><e>to<g>service</g></e>"))

        
        self.assertEqual(remove_tag.parent, None)
        self.assertEqual(remove_tag.find(text="right").next_element, None)
        self.assertEqual(remove_tag.previous_element, None)
        self.assertEqual(remove_tag.next_sibling, None)
        self.assertEqual(remove_tag.previous_sibling, None)

        
        self.assertEqual(move_tag.parent, soup.a)
        self.assertEqual(move_tag.previous_element, "We")
        self.assertEqual(move_tag.next_element.next_element, soup.e)
        self.assertEqual(move_tag.next_sibling, None)

        
        
        to_text = soup.find(text="to")
        g_tag = soup.g
        self.assertEqual(to_text.next_element, g_tag)
        self.assertEqual(to_text.next_sibling, g_tag)
        self.assertEqual(g_tag.previous_element, to_text)
        self.assertEqual(g_tag.previous_sibling, to_text)

    def test_unwrap(self):
        tree = self.soup()
        tree.em.unwrap()
        self.assertEqual(tree.em, None)
        self.assertEqual(tree.p.text, "Unneeded formatting is unneeded")

    def test_wrap(self):
        soup = self.soup("I wish I was bold.")
        value = soup.string.wrap(soup.new_tag("b"))
        self.assertEqual(value.decode(), "<b>I wish I was bold.</b>")
        self.assertEqual(
            soup.decode(), self.document_for("<b>I wish I was bold.</b>"))

    def test_wrap_extracts_tag_from_elsewhere(self):
        soup = self.soup("<b></b>I wish I was bold.")
        soup.b.next_sibling.wrap(soup.b)
        self.assertEqual(
            soup.decode(), self.document_for("<b>I wish I was bold.</b>"))

    def test_wrap_puts_new_contents_at_the_end(self):
        soup = self.soup("<b>I like being bold.</b>I wish I was bold.")
        soup.b.next_sibling.wrap(soup.b)
        self.assertEqual(2, len(soup.b.contents))
        self.assertEqual(
            soup.decode(), self.document_for(
                "<b>I like being bold.I wish I was bold.</b>"))

    def test_extract(self):
        soup = self.soup(
            '<html><body>Some content. <div id="nav">Nav crap</div> More content.</body></html>')

        self.assertEqual(len(soup.body.contents), 3)
        extracted = soup.find(id="nav").extract()

        self.assertEqual(
            soup.decode(), "<html><body>Some content.  More content.</body></html>")
        self.assertEqual(extracted.decode(), '<div id="nav">Nav crap</div>')

        
        self.assertEqual(len(soup.body.contents), 2)
        self.assertEqual(extracted.parent, None)
        self.assertEqual(extracted.previous_element, None)
        self.assertEqual(extracted.next_element.next_element, None)

        
        content_1 = soup.find(text="Some content. ")
        content_2 = soup.find(text=" More content.")
        self.assertEqual(content_1.next_element, content_2)
        self.assertEqual(content_1.next_sibling, content_2)
        self.assertEqual(content_2.previous_element, content_1)
        self.assertEqual(content_2.previous_sibling, content_1)

    def test_extract_distinguishes_between_identical_strings(self):
        soup = self.soup("<a>foo</a><b>bar</b>")
        foo_1 = soup.a.string
        bar_1 = soup.b.string
        foo_2 = soup.new_string("foo")
        bar_2 = soup.new_string("bar")
        soup.a.append(foo_2)
        soup.b.append(bar_2)

        
        
        
        foo_1.extract()
        bar_2.extract()
        self.assertEqual(foo_2, soup.a.string)
        self.assertEqual(bar_2, soup.b.string)

    def test_clear(self):
        
        soup = self.soup("<p><a>String <em>Italicized</em></a> and another</p>")
        
        a = soup.a
        soup.p.clear()
        self.assertEqual(len(soup.p.contents), 0)
        self.assertTrue(hasattr(a, "contents"))

        
        em = a.em
        a.clear(decompose=True)
        self.assertFalse(hasattr(em, "contents"))

    def test_string_set(self):
        
        soup = self.soup("<a></a> <b><c></c></b>")
        soup.a.string = "foo"
        self.assertEqual(soup.a.contents, ["foo"])
        soup.b.string = "bar"
        self.assertEqual(soup.b.contents, ["bar"])

    def test_string_set_does_not_affect_original_string(self):
        soup = self.soup("<a><b>foo</b><c>bar</c>")
        soup.b.string = soup.c.string
        self.assertEqual(soup.a.encode(), b"<a><b>bar</b><c>bar</c></a>")

    def test_set_string_preserves_class_of_string(self):
        soup = self.soup("<a></a>")
        cdata = CData("foo")
        soup.a.string = cdata
        self.assertTrue(isinstance(soup.a.string, CData))

class TestElementObjects(SoupTest):
    

    def test_len(self):
        
        soup = self.soup("<top>1<b>2</b>3</top>")

        
        
        self.assertEqual(len(soup.contents), 1)
        self.assertEqual(len(soup), 1)

        
        
        self.assertEqual(len(soup.top), 3)
        self.assertEqual(len(soup.top.contents), 3)

    def test_member_access_invokes_find(self):
        
        soup = self.soup('<b><i></i></b>')
        self.assertEqual(soup.b, soup.find('b'))
        self.assertEqual(soup.b.i, soup.find('b').find('i'))
        self.assertEqual(soup.a, None)

    def test_deprecated_member_access(self):
        soup = self.soup('<b><i></i></b>')
        with warnings.catch_warnings(record=True) as w:
            tag = soup.bTag
        self.assertEqual(soup.b, tag)
        self.assertEqual(
            '.bTag is deprecated, use .find("b") instead.',
            str(w[0].message))

    def test_has_attr(self):
        
        soup = self.soup("<foo attr='bar'>")
        self.assertTrue(soup.foo.has_attr('attr'))
        self.assertFalse(soup.foo.has_attr('attr2'))


    def test_attributes_come_out_in_alphabetical_order(self):
        markup = '<b a="1" z="5" m="3" f="2" y="4"></b>'
        self.assertSoupEquals(markup, '<b a="1" f="2" m="3" y="4" z="5"></b>')

    def test_string(self):
        
        
        soup = self.soup("<b>foo</b>")
        self.assertEqual(soup.b.string, 'foo')

    def test_empty_tag_has_no_string(self):
        
        soup = self.soup("<b></b>")
        self.assertEqual(soup.b.string, None)

    def test_tag_with_multiple_children_has_no_string(self):
        
        soup = self.soup("<a>foo<b></b><b></b></b>")
        self.assertEqual(soup.b.string, None)

        soup = self.soup("<a>foo<b></b>bar</b>")
        self.assertEqual(soup.b.string, None)

        
        
        soup = self.soup("<a>foo</b>")
        soup.a.insert(1, "bar")
        self.assertEqual(soup.a.string, None)

    def test_tag_with_recursive_string_has_string(self):
        
        
        soup = self.soup("<a><b>foo</b></a>")
        self.assertEqual(soup.a.string, "foo")
        self.assertEqual(soup.string, "foo")

    def test_lack_of_string(self):
        
        soup = self.soup("<b>f<i>e</i>o</b>")
        self.assertFalse(soup.b.string)

        soup = self.soup("<b></b>")
        self.assertFalse(soup.b.string)

    def test_all_text(self):
        
        soup = self.soup("<a>a<b>r</b>   <r> t </r></a>")
        self.assertEqual(soup.a.text, "ar  t ")
        self.assertEqual(soup.a.get_text(strip=True), "art")
        self.assertEqual(soup.a.get_text(","), "a,r, , t ")
        self.assertEqual(soup.a.get_text(",", strip=True), "a,r,t")

class TestCDAtaListAttributes(SoupTest):

    
    def test_single_value_becomes_list(self):
        soup = self.soup("<a class='foo'>")
        self.assertEqual(["foo"],soup.a['class'])

    def test_multiple_values_becomes_list(self):
        soup = self.soup("<a class='foo bar'>")
        self.assertEqual(["foo", "bar"], soup.a['class'])

    def test_multiple_values_separated_by_weird_whitespace(self):
        soup = self.soup("<a class='foo\tbar\nbaz'>")
        self.assertEqual(["foo", "bar", "baz"],soup.a['class'])

    def test_attributes_joined_into_string_on_output(self):
        soup = self.soup("<a class='foo\tbar'>")
        self.assertEqual(b'<a class="foo bar"></a>', soup.a.encode())

    def test_accept_charset(self):
        soup = self.soup('<form accept-charset="ISO-8859-1 UTF-8">')
        self.assertEqual(['ISO-8859-1', 'UTF-8'], soup.form['accept-charset'])

    def test_cdata_attribute_applying_only_to_one_tag(self):
        data = '<a accept-charset="ISO-8859-1 UTF-8"></a>'
        soup = self.soup(data)
        
        
        
        self.assertEqual('ISO-8859-1 UTF-8', soup.a['accept-charset'])


class TestPersistence(SoupTest):
    "Testing features like pickle and deepcopy."

    def setUp(self):
        super(TestPersistence, self).setUp()
        self.page = 
        self.tree = self.soup(self.page)

    def test_pickle_and_unpickle_identity(self):
        
        
        dumped = pickle.dumps(self.tree, 2)
        loaded = pickle.loads(dumped)
        self.assertEqual(loaded.__class__, BeautifulSoup)
        self.assertEqual(loaded.decode(), self.tree.decode())

    def test_deepcopy_identity(self):
        
        copied = copy.deepcopy(self.tree)
        self.assertEqual(copied.decode(), self.tree.decode())

    def test_unicode_pickle(self):
        
        html = u"<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        dumped = pickle.dumps(soup, pickle.HIGHEST_PROTOCOL)
        loaded = pickle.loads(dumped)
        self.assertEqual(loaded.decode(), soup.decode())


class TestSubstitutions(SoupTest):

    def test_default_formatter_is_minimal(self):
        markup = u"<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter="minimal")
        
        self.assertEqual(
            decoded,
            self.document_for(
                u"<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"))

    def test_formatter_html(self):
        markup = u"<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter="html")
        self.assertEqual(
            decoded,
            self.document_for("<b>&lt;&lt;Sacr&eacute; bleu!&gt;&gt;</b>"))

    def test_formatter_minimal(self):
        markup = u"<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter="minimal")
        
        self.assertEqual(
            decoded,
            self.document_for(
                u"<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"))

    def test_formatter_null(self):
        markup = u"<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter=None)
        
        
        self.assertEqual(decoded,
                          self.document_for(u"<b><<Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!>></b>"))

    def test_formatter_custom(self):
        markup = u"<b>&lt;foo&gt;</b><b>bar</b>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter = lambda x: x.upper())
        
        
        self.assertEqual(
            decoded,
            self.document_for(u"<b><FOO></b><b>BAR</b>"))

    def test_formatter_is_run_on_attribute_values(self):
        markup = u'<a href="http://a.com?a=b&c=é">e</a>'
        soup = self.soup(markup)
        a = soup.a

        expect_minimal = u'<a href="http://a.com?a=b&amp;c=é">e</a>'

        self.assertEqual(expect_minimal, a.decode())
        self.assertEqual(expect_minimal, a.decode(formatter="minimal"))

        expect_html = u'<a href="http://a.com?a=b&amp;c=&eacute;">e</a>'
        self.assertEqual(expect_html, a.decode(formatter="html"))

        self.assertEqual(markup, a.decode(formatter=None))
        expect_upper = u'<a href="HTTP://A.COM?A=B&C=É">E</a>'
        self.assertEqual(expect_upper, a.decode(formatter=lambda x: x.upper()))

    def test_prettify_accepts_formatter(self):
        soup = BeautifulSoup("<html><body>foo</body></html>")
        pretty = soup.prettify(formatter = lambda x: x.upper())
        self.assertTrue("FOO" in pretty)

    def test_prettify_outputs_unicode_by_default(self):
        soup = self.soup("<a></a>")
        self.assertEqual(unicode, type(soup.prettify()))

    def test_prettify_can_encode_data(self):
        soup = self.soup("<a></a>")
        self.assertEqual(bytes, type(soup.prettify("utf-8")))

    def test_html_entity_substitution_off_by_default(self):
        markup = u"<b>Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!</b>"
        soup = self.soup(markup)
        encoded = soup.b.encode("utf-8")
        self.assertEqual(encoded, markup.encode('utf-8'))

    def test_encoding_substitution(self):
        
        
        meta_tag = ('<meta content="text/html; charset=x-sjis" '
                    'http-equiv="Content-type"/>')
        soup = self.soup(meta_tag)

        
        self.assertEqual(soup.meta['content'], 'text/html; charset=x-sjis')

        
        
        utf_8 = soup.encode("utf-8")
        self.assertTrue(b"charset=utf-8" in utf_8)

        euc_jp = soup.encode("euc_jp")
        self.assertTrue(b"charset=euc_jp" in euc_jp)

        shift_jis = soup.encode("shift-jis")
        self.assertTrue(b"charset=shift-jis" in shift_jis)

        utf_16_u = soup.encode("utf-16").decode("utf-16")
        self.assertTrue("charset=utf-16" in utf_16_u)

    def test_encoding_substitution_doesnt_happen_if_tag_is_strained(self):
        markup = ('<head><meta content="text/html; charset=x-sjis" '
                    'http-equiv="Content-type"/></head><pre>foo</pre>')

        
        
        
        strainer = SoupStrainer('pre')
        soup = self.soup(markup, parse_only=strainer)
        self.assertEqual(soup.contents[0].name, 'pre')

class TestEncoding(SoupTest):
    

    def test_unicode_string_can_be_encoded(self):
        html = u"<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        self.assertEqual(soup.b.string.encode("utf-8"),
                          u"\N{SNOWMAN}".encode("utf-8"))

    def test_tag_containing_unicode_string_can_be_encoded(self):
        html = u"<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        self.assertEqual(
            soup.b.encode("utf-8"), html.encode("utf-8"))

    def test_encoding_substitutes_unrecognized_characters_by_default(self):
        html = u"<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        self.assertEqual(soup.b.encode("ascii"), b"<b>&

    def test_encoding_can_be_made_strict(self):
        html = u"<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        self.assertRaises(
            UnicodeEncodeError, soup.encode, "ascii", errors="strict")

    def test_decode_contents(self):
        html = u"<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        self.assertEqual(u"\N{SNOWMAN}", soup.b.decode_contents())

    def test_encode_contents(self):
        html = u"<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        self.assertEqual(
            u"\N{SNOWMAN}".encode("utf8"), soup.b.encode_contents(
                encoding="utf8"))

    def test_deprecated_renderContents(self):
        html = u"<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        self.assertEqual(
            u"\N{SNOWMAN}".encode("utf8"), soup.b.renderContents())

class TestNavigableStringSubclasses(SoupTest):

    def test_cdata(self):
        
        
        soup = self.soup("")
        cdata = CData("foo")
        soup.insert(1, cdata)
        self.assertEqual(str(soup), "<![CDATA[foo]]>")
        self.assertEqual(soup.find(text="foo"), "foo")
        self.assertEqual(soup.contents[0], "foo")

    def test_cdata_is_never_formatted(self):
        

        self.count = 0
        def increment(*args):
            self.count += 1
            return "BITTER FAILURE"

        soup = self.soup("")
        cdata = CData("<><><>")
        soup.insert(1, cdata)
        self.assertEqual(
            b"<![CDATA[<><><>]]>", soup.encode(formatter=increment))
        self.assertEqual(1, self.count)

    def test_doctype_ends_in_newline(self):
        
        
        doctype = Doctype("foo")
        soup = self.soup("")
        soup.insert(1, doctype)
        self.assertEqual(soup.encode(), b"<!DOCTYPE foo>\n")


class TestSoupSelector(TreeTest):

    HTML = 

    def setUp(self):
        self.soup = BeautifulSoup(self.HTML)

    def assertSelects(self, selector, expected_ids):
        el_ids = [el['id'] for el in self.soup.select(selector)]
        el_ids.sort()
        expected_ids.sort()
        self.assertEqual(expected_ids, el_ids,
            "Selector %s, expected [%s], got [%s]" % (
                selector, ', '.join(expected_ids), ', '.join(el_ids)
            )
        )

    assertSelect = assertSelects

    def assertSelectMultiple(self, *tests):
        for selector, expected_ids in tests:
            self.assertSelect(selector, expected_ids)

    def test_one_tag_one(self):
        els = self.soup.select('title')
        self.assertEqual(len(els), 1)
        self.assertEqual(els[0].name, 'title')
        self.assertEqual(els[0].contents, [u'The title'])

    def test_one_tag_many(self):
        els = self.soup.select('div')
        self.assertEqual(len(els), 3)
        for div in els:
            self.assertEqual(div.name, 'div')

    def test_tag_in_tag_one(self):
        els = self.soup.select('div div')
        self.assertSelects('div div', ['inner'])

    def test_tag_in_tag_many(self):
        for selector in ('html div', 'html body div', 'body div'):
            self.assertSelects(selector, ['main', 'inner', 'footer'])

    def test_tag_no_match(self):
        self.assertEqual(len(self.soup.select('del')), 0)

    def test_invalid_tag(self):
        self.assertEqual(len(self.soup.select('tag%t')), 0)

    def test_header_tags(self):
        self.assertSelectMultiple(
            ('h1', ['header1']),
            ('h2', ['header2', 'header3']),
        )

    def test_class_one(self):
        for selector in ('.onep', 'p.onep', 'html p.onep'):
            els = self.soup.select(selector)
            self.assertEqual(len(els), 1)
            self.assertEqual(els[0].name, 'p')
            self.assertEqual(els[0]['class'], ['onep'])

    def test_class_mismatched_tag(self):
        els = self.soup.select('div.onep')
        self.assertEqual(len(els), 0)

    def test_one_id(self):
        for selector in ('div
            self.assertSelects(selector, ['inner'])

    def test_bad_id(self):
        els = self.soup.select('#doesnotexist')
        self.assertEqual(len(els), 0)

    def test_items_in_id(self):
        els = self.soup.select('div
        self.assertEqual(len(els), 3)
        for el in els:
            self.assertEqual(el.name, 'p')
        self.assertEqual(els[1]['class'], ['onep'])
        self.assertFalse(els[0].has_key('class'))

    def test_a_bunch_of_emptys(self):
        for selector in ('div
            self.assertEqual(len(self.soup.select(selector)), 0)

    def test_multi_class_support(self):
        for selector in ('.class1', 'p.class1', '.class2', 'p.class2',
            '.class3', 'p.class3', 'html p.class2', 'div
            self.assertSelects(selector, ['pmulti'])

    def test_multi_class_selection(self):
        for selector in ('.class1.class3', '.class3.class2',
                         '.class1.class2.class3'):
            self.assertSelects(selector, ['pmulti'])

    def test_child_selector(self):
        self.assertSelects('.s1 > a', ['s1a1', 's1a2'])
        self.assertSelects('.s1 > a span', ['s1a2s1'])

    def test_attribute_equals(self):
        self.assertSelectMultiple(
            ('p[class="onep"]', ['p1']),
            ('p[id="p1"]', ['p1']),
            ('[class="onep"]', ['p1']),
            ('[id="p1"]', ['p1']),
            ('link[rel="stylesheet"]', ['l1']),
            ('link[type="text/css"]', ['l1']),
            ('link[href="blah.css"]', ['l1']),
            ('link[href="no-blah.css"]', []),
            ('[rel="stylesheet"]', ['l1']),
            ('[type="text/css"]', ['l1']),
            ('[href="blah.css"]', ['l1']),
            ('[href="no-blah.css"]', []),
            ('p[href="no-blah.css"]', []),
            ('[href="no-blah.css"]', []),
        )

    def test_attribute_tilde(self):
        self.assertSelectMultiple(
            ('p[class~="class1"]', ['pmulti']),
            ('p[class~="class2"]', ['pmulti']),
            ('p[class~="class3"]', ['pmulti']),
            ('[class~="class1"]', ['pmulti']),
            ('[class~="class2"]', ['pmulti']),
            ('[class~="class3"]', ['pmulti']),
            ('a[rel~="friend"]', ['bob']),
            ('a[rel~="met"]', ['bob']),
            ('[rel~="friend"]', ['bob']),
            ('[rel~="met"]', ['bob']),
        )

    def test_attribute_startswith(self):
        self.assertSelectMultiple(
            ('[rel^="style"]', ['l1']),
            ('link[rel^="style"]', ['l1']),
            ('notlink[rel^="notstyle"]', []),
            ('[rel^="notstyle"]', []),
            ('link[rel^="notstyle"]', []),
            ('link[href^="bla"]', ['l1']),
            ('a[href^="http://"]', ['bob', 'me']),
            ('[href^="http://"]', ['bob', 'me']),
            ('[id^="p"]', ['pmulti', 'p1']),
            ('[id^="m"]', ['me', 'main']),
            ('div[id^="m"]', ['main']),
            ('a[id^="m"]', ['me']),
        )

    def test_attribute_endswith(self):
        self.assertSelectMultiple(
            ('[href$=".css"]', ['l1']),
            ('link[href$=".css"]', ['l1']),
            ('link[id$="1"]', ['l1']),
            ('[id$="1"]', ['l1', 'p1', 'header1', 's1a1', 's2a1', 's1a2s1']),
            ('div[id$="1"]', []),
            ('[id$="noending"]', []),
        )

    def test_attribute_contains(self):
        self.assertSelectMultiple(
            
            ('[rel*="style"]', ['l1']),
            ('link[rel*="style"]', ['l1']),
            ('notlink[rel*="notstyle"]', []),
            ('[rel*="notstyle"]', []),
            ('link[rel*="notstyle"]', []),
            ('link[href*="bla"]', ['l1']),
            ('a[href*="http://"]', ['bob', 'me']),
            ('[href*="http://"]', ['bob', 'me']),
            ('[id*="p"]', ['pmulti', 'p1']),
            ('div[id*="m"]', ['main']),
            ('a[id*="m"]', ['me']),
            
            ('[href*=".css"]', ['l1']),
            ('link[href*=".css"]', ['l1']),
            ('link[id*="1"]', ['l1']),
            ('[id*="1"]', ['l1', 'p1', 'header1', 's1a1', 's1a2', 's2a1', 's1a2s1']),
            ('div[id*="1"]', []),
            ('[id*="noending"]', []),
            
            ('[href*="."]', ['bob', 'me', 'l1']),
            ('a[href*="."]', ['bob', 'me']),
            ('link[href*="."]', ['l1']),
            ('div[id*="n"]', ['main', 'inner']),
            ('div[id*="nn"]', ['inner']),
        )

    def test_attribute_exact_or_hypen(self):
        self.assertSelectMultiple(
            ('p[lang|="en"]', ['lang-en', 'lang-en-gb', 'lang-en-us']),
            ('[lang|="en"]', ['lang-en', 'lang-en-gb', 'lang-en-us']),
            ('p[lang|="fr"]', ['lang-fr']),
            ('p[lang|="gb"]', []),
        )

    def test_attribute_exists(self):
        self.assertSelectMultiple(
            ('[rel]', ['l1', 'bob', 'me']),
            ('link[rel]', ['l1']),
            ('a[rel]', ['bob', 'me']),
            ('[lang]', ['lang-en', 'lang-en-gb', 'lang-en-us', 'lang-fr']),
            ('p[class]', ['p1', 'pmulti']),
            ('[blah]', []),
            ('p[blah]', []),
        )

    def test_select_on_element(self):
        
        
        inner = self.soup.find("div", id="main")
        selected = inner.select("div")
        
        
        self.assertSelectsIDs(selected, ['inner'])
