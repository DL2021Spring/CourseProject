


import codecs
from htmlentitydefs import codepoint2name
import re
import logging


chardet_type = None
try:
    
    
    import cchardet
    def chardet_dammit(s):
        return cchardet.detect(s)['encoding']
except ImportError:
    try:
        
        
        
        import chardet
        def chardet_dammit(s):
            return chardet.detect(s)['encoding']
        
        
    except ImportError:
        
        def chardet_dammit(s):
            return None


try:
    import iconv_codec
except ImportError:
    pass

xml_encoding_re = re.compile(
    '^<\?.*encoding=[\'"](.*?)[\'"].*\?>'.encode(), re.I)
html_meta_re = re.compile(
    '<\s*meta[^>]+charset\s*=\s*["\']?([^>]*?)[ /;\'">]'.encode(), re.I)

class EntitySubstitution(object):

    

    def _populate_class_variables():
        lookup = {}
        reverse_lookup = {}
        characters_for_re = []
        for codepoint, name in list(codepoint2name.items()):
            character = unichr(codepoint)
            if codepoint != 34:
                
                
                
                characters_for_re.append(character)
                lookup[character] = name
            
            reverse_lookup[name] = character
        re_definition = "[%s]" % "".join(characters_for_re)
        return lookup, reverse_lookup, re.compile(re_definition)
    (CHARACTER_TO_HTML_ENTITY, HTML_ENTITY_TO_CHARACTER,
     CHARACTER_TO_HTML_ENTITY_RE) = _populate_class_variables()

    CHARACTER_TO_XML_ENTITY = {
        "'": "apos",
        '"': "quot",
        "&": "amp",
        "<": "lt",
        ">": "gt",
        }

    BARE_AMPERSAND_OR_BRACKET = re.compile("([<>]|"
                                           "&(?!
                                           ")")

    @classmethod
    def _substitute_html_entity(cls, matchobj):
        entity = cls.CHARACTER_TO_HTML_ENTITY.get(matchobj.group(0))
        return "&%s;" % entity

    @classmethod
    def _substitute_xml_entity(cls, matchobj):
        
        entity = cls.CHARACTER_TO_XML_ENTITY[matchobj.group(0)]
        return "&%s;" % entity

    @classmethod
    def quoted_attribute_value(self, value):
        
        quote_with = '"'
        if '"' in value:
            if "'" in value:
                
                
                
                
                
                
                
                replace_with = "&quot;"
                value = value.replace('"', replace_with)
            else:
                
                
                quote_with = "'"
        return quote_with + value + quote_with

    @classmethod
    def substitute_xml(cls, value, make_quoted_attribute=False):
        
        
        
        value = cls.BARE_AMPERSAND_OR_BRACKET.sub(
            cls._substitute_xml_entity, value)

        if make_quoted_attribute:
            value = cls.quoted_attribute_value(value)
        return value

    @classmethod
    def substitute_html(cls, s):
        
        return cls.CHARACTER_TO_HTML_ENTITY_RE.sub(
            cls._substitute_html_entity, s)


class UnicodeDammit:
    

    
    
    
    
    CHARSET_ALIASES = {"macintosh": "mac-roman",
                       "x-sjis": "shift-jis"}

    ENCODINGS_WITH_SMART_QUOTES = [
        "windows-1252",
        "iso-8859-1",
        "iso-8859-2",
        ]

    def __init__(self, markup, override_encodings=[],
                 smart_quotes_to=None, is_html=False):
        self.declared_html_encoding = None
        self.smart_quotes_to = smart_quotes_to
        self.tried_encodings = []
        self.contains_replacement_characters = False

        if markup == '' or isinstance(markup, unicode):
            self.markup = markup
            self.unicode_markup = unicode(markup)
            self.original_encoding = None
            return

        new_markup, document_encoding, sniffed_encoding = \
            self._detectEncoding(markup, is_html)
        self.markup = new_markup

        u = None
        if new_markup != markup:
            
            
            u = self._convert_from("utf8")
            self.original_encoding = sniffed_encoding

        if not u:
            for proposed_encoding in (
                override_encodings + [document_encoding, sniffed_encoding]):
                if proposed_encoding is not None:
                    u = self._convert_from(proposed_encoding)
                    if u:
                        break

        
        if not u and not isinstance(self.markup, unicode):
            u = self._convert_from(chardet_dammit(self.markup))

        
        if not u:
            for proposed_encoding in ("utf-8", "windows-1252"):
                u = self._convert_from(proposed_encoding)
                if u:
                    break

        
        
        if not u:
            for proposed_encoding in (
                override_encodings + [
                    document_encoding, sniffed_encoding, "utf-8", "windows-1252"]):
                if proposed_encoding != "ascii":
                    u = self._convert_from(proposed_encoding, "replace")
                if u is not None:
                    logging.warning(
                            "Some characters could not be decoded, and were "
                            "replaced with REPLACEMENT CHARACTER.")
                    self.contains_replacement_characters = True
                    break

        
        
        self.unicode_markup = u
        if not u:
            self.original_encoding = None

    def _sub_ms_char(self, match):
        
        orig = match.group(1)
        if self.smart_quotes_to == 'ascii':
            sub = self.MS_CHARS_TO_ASCII.get(orig).encode()
        else:
            sub = self.MS_CHARS.get(orig)
            if type(sub) == tuple:
                if self.smart_quotes_to == 'xml':
                    sub = '&
                else:
                    sub = '&'.encode() + sub[0].encode() + ';'.encode()
            else:
                sub = sub.encode()
        return sub

    def _convert_from(self, proposed, errors="strict"):
        proposed = self.find_codec(proposed)
        if not proposed or (proposed, errors) in self.tried_encodings:
            return None
        self.tried_encodings.append((proposed, errors))
        markup = self.markup

        
        
        if (self.smart_quotes_to is not None
            and proposed.lower() in self.ENCODINGS_WITH_SMART_QUOTES):
            smart_quotes_re = b"([\x80-\x9f])"
            smart_quotes_compiled = re.compile(smart_quotes_re)
            markup = smart_quotes_compiled.sub(self._sub_ms_char, markup)

        try:
            
            
            u = self._to_unicode(markup, proposed, errors)
            self.markup = u
            self.original_encoding = proposed
        except Exception as e:
            
            
            return None
        
        return self.markup

    def _to_unicode(self, data, encoding, errors="strict"):
        

        
        if (len(data) >= 4) and (data[:2] == '\xfe\xff') \
               and (data[2:4] != '\x00\x00'):
            encoding = 'utf-16be'
            data = data[2:]
        elif (len(data) >= 4) and (data[:2] == '\xff\xfe') \
                 and (data[2:4] != '\x00\x00'):
            encoding = 'utf-16le'
            data = data[2:]
        elif data[:3] == '\xef\xbb\xbf':
            encoding = 'utf-8'
            data = data[3:]
        elif data[:4] == '\x00\x00\xfe\xff':
            encoding = 'utf-32be'
            data = data[4:]
        elif data[:4] == '\xff\xfe\x00\x00':
            encoding = 'utf-32le'
            data = data[4:]
        newdata = unicode(data, encoding, errors)
        return newdata

    def _detectEncoding(self, xml_data, is_html=False):
        
        xml_encoding = sniffed_xml_encoding = None
        try:
            if xml_data[:4] == b'\x4c\x6f\xa7\x94':
                
                xml_data = self._ebcdic_to_ascii(xml_data)
            elif xml_data[:4] == b'\x00\x3c\x00\x3f':
                
                sniffed_xml_encoding = 'utf-16be'
                xml_data = unicode(xml_data, 'utf-16be').encode('utf-8')
            elif (len(xml_data) >= 4) and (xml_data[:2] == b'\xfe\xff') \
                     and (xml_data[2:4] != b'\x00\x00'):
                
                sniffed_xml_encoding = 'utf-16be'
                xml_data = unicode(xml_data[2:], 'utf-16be').encode('utf-8')
            elif xml_data[:4] == b'\x3c\x00\x3f\x00':
                
                sniffed_xml_encoding = 'utf-16le'
                xml_data = unicode(xml_data, 'utf-16le').encode('utf-8')
            elif (len(xml_data) >= 4) and (xml_data[:2] == b'\xff\xfe') and \
                     (xml_data[2:4] != b'\x00\x00'):
                
                sniffed_xml_encoding = 'utf-16le'
                xml_data = unicode(xml_data[2:], 'utf-16le').encode('utf-8')
            elif xml_data[:4] == b'\x00\x00\x00\x3c':
                
                sniffed_xml_encoding = 'utf-32be'
                xml_data = unicode(xml_data, 'utf-32be').encode('utf-8')
            elif xml_data[:4] == b'\x3c\x00\x00\x00':
                
                sniffed_xml_encoding = 'utf-32le'
                xml_data = unicode(xml_data, 'utf-32le').encode('utf-8')
            elif xml_data[:4] == b'\x00\x00\xfe\xff':
                
                sniffed_xml_encoding = 'utf-32be'
                xml_data = unicode(xml_data[4:], 'utf-32be').encode('utf-8')
            elif xml_data[:4] == b'\xff\xfe\x00\x00':
                
                sniffed_xml_encoding = 'utf-32le'
                xml_data = unicode(xml_data[4:], 'utf-32le').encode('utf-8')
            elif xml_data[:3] == b'\xef\xbb\xbf':
                
                sniffed_xml_encoding = 'utf-8'
                xml_data = unicode(xml_data[3:], 'utf-8').encode('utf-8')
            else:
                sniffed_xml_encoding = 'ascii'
                pass
        except:
            xml_encoding_match = None
        xml_encoding_match = xml_encoding_re.match(xml_data)
        if not xml_encoding_match and is_html:
            xml_encoding_match = html_meta_re.search(xml_data)
        if xml_encoding_match is not None:
            xml_encoding = xml_encoding_match.groups()[0].decode(
                'ascii').lower()
            if is_html:
                self.declared_html_encoding = xml_encoding
            if sniffed_xml_encoding and \
               (xml_encoding in ('iso-10646-ucs-2', 'ucs-2', 'csunicode',
                                 'iso-10646-ucs-4', 'ucs-4', 'csucs4',
                                 'utf-16', 'utf-32', 'utf_16', 'utf_32',
                                 'utf16', 'u16')):
                xml_encoding = sniffed_xml_encoding
        return xml_data, xml_encoding, sniffed_xml_encoding

    def find_codec(self, charset):
        return self._codec(self.CHARSET_ALIASES.get(charset, charset)) \
               or (charset and self._codec(charset.replace("-", ""))) \
               or (charset and self._codec(charset.replace("-", "_"))) \
               or charset

    def _codec(self, charset):
        if not charset:
            return charset
        codec = None
        try:
            codecs.lookup(charset)
            codec = charset
        except (LookupError, ValueError):
            pass
        return codec

    EBCDIC_TO_ASCII_MAP = None

    def _ebcdic_to_ascii(self, s):
        c = self.__class__
        if not c.EBCDIC_TO_ASCII_MAP:
            emap = (0,1,2,3,156,9,134,127,151,141,142,11,12,13,14,15,
                    16,17,18,19,157,133,8,135,24,25,146,143,28,29,30,31,
                    128,129,130,131,132,10,23,27,136,137,138,139,140,5,6,7,
                    144,145,22,147,148,149,150,4,152,153,154,155,20,21,158,26,
                    32,160,161,162,163,164,165,166,167,168,91,46,60,40,43,33,
                    38,169,170,171,172,173,174,175,176,177,93,36,42,41,59,94,
                    45,47,178,179,180,181,182,183,184,185,124,44,37,95,62,63,
                    186,187,188,189,190,191,192,193,194,96,58,35,64,39,61,34,
                    195,97,98,99,100,101,102,103,104,105,196,197,198,199,200,
                    201,202,106,107,108,109,110,111,112,113,114,203,204,205,
                    206,207,208,209,126,115,116,117,118,119,120,121,122,210,
                    211,212,213,214,215,216,217,218,219,220,221,222,223,224,
                    225,226,227,228,229,230,231,123,65,66,67,68,69,70,71,72,
                    73,232,233,234,235,236,237,125,74,75,76,77,78,79,80,81,
                    82,238,239,240,241,242,243,92,159,83,84,85,86,87,88,89,
                    90,244,245,246,247,248,249,48,49,50,51,52,53,54,55,56,57,
                    250,251,252,253,254,255)
            import string
            c.EBCDIC_TO_ASCII_MAP = string.maketrans(
            ''.join(map(chr, list(range(256)))), ''.join(map(chr, emap)))
        return s.translate(c.EBCDIC_TO_ASCII_MAP)

    
    MS_CHARS = {b'\x80': ('euro', '20AC'),
                b'\x81': ' ',
                b'\x82': ('sbquo', '201A'),
                b'\x83': ('fnof', '192'),
                b'\x84': ('bdquo', '201E'),
                b'\x85': ('hellip', '2026'),
                b'\x86': ('dagger', '2020'),
                b'\x87': ('Dagger', '2021'),
                b'\x88': ('circ', '2C6'),
                b'\x89': ('permil', '2030'),
                b'\x8A': ('Scaron', '160'),
                b'\x8B': ('lsaquo', '2039'),
                b'\x8C': ('OElig', '152'),
                b'\x8D': '?',
                b'\x8E': ('#x17D', '17D'),
                b'\x8F': '?',
                b'\x90': '?',
                b'\x91': ('lsquo', '2018'),
                b'\x92': ('rsquo', '2019'),
                b'\x93': ('ldquo', '201C'),
                b'\x94': ('rdquo', '201D'),
                b'\x95': ('bull', '2022'),
                b'\x96': ('ndash', '2013'),
                b'\x97': ('mdash', '2014'),
                b'\x98': ('tilde', '2DC'),
                b'\x99': ('trade', '2122'),
                b'\x9a': ('scaron', '161'),
                b'\x9b': ('rsaquo', '203A'),
                b'\x9c': ('oelig', '153'),
                b'\x9d': '?',
                b'\x9e': ('#x17E', '17E'),
                b'\x9f': ('Yuml', ''),}

    
    
    
    MS_CHARS_TO_ASCII = {
        b'\x80' : 'EUR',
        b'\x81' : ' ',
        b'\x82' : ',',
        b'\x83' : 'f',
        b'\x84' : ',,',
        b'\x85' : '...',
        b'\x86' : '+',
        b'\x87' : '++',
        b'\x88' : '^',
        b'\x89' : '%',
        b'\x8a' : 'S',
        b'\x8b' : '<',
        b'\x8c' : 'OE',
        b'\x8d' : '?',
        b'\x8e' : 'Z',
        b'\x8f' : '?',
        b'\x90' : '?',
        b'\x91' : "'",
        b'\x92' : "'",
        b'\x93' : '"',
        b'\x94' : '"',
        b'\x95' : '*',
        b'\x96' : '-',
        b'\x97' : '--',
        b'\x98' : '~',
        b'\x99' : '(TM)',
        b'\x9a' : 's',
        b'\x9b' : '>',
        b'\x9c' : 'oe',
        b'\x9d' : '?',
        b'\x9e' : 'z',
        b'\x9f' : 'Y',
        b'\xa0' : ' ',
        b'\xa1' : '!',
        b'\xa2' : 'c',
        b'\xa3' : 'GBP',
        b'\xa4' : '$', 
                       
        b'\xa5' : 'YEN',
        b'\xa6' : '|',
        b'\xa7' : 'S',
        b'\xa8' : '..',
        b'\xa9' : '',
        b'\xaa' : '(th)',
        b'\xab' : '<<',
        b'\xac' : '!',
        b'\xad' : ' ',
        b'\xae' : '(R)',
        b'\xaf' : '-',
        b'\xb0' : 'o',
        b'\xb1' : '+-',
        b'\xb2' : '2',
        b'\xb3' : '3',
        b'\xb4' : ("'", 'acute'),
        b'\xb5' : 'u',
        b'\xb6' : 'P',
        b'\xb7' : '*',
        b'\xb8' : ',',
        b'\xb9' : '1',
        b'\xba' : '(th)',
        b'\xbb' : '>>',
        b'\xbc' : '1/4',
        b'\xbd' : '1/2',
        b'\xbe' : '3/4',
        b'\xbf' : '?',
        b'\xc0' : 'A',
        b'\xc1' : 'A',
        b'\xc2' : 'A',
        b'\xc3' : 'A',
        b'\xc4' : 'A',
        b'\xc5' : 'A',
        b'\xc6' : 'AE',
        b'\xc7' : 'C',
        b'\xc8' : 'E',
        b'\xc9' : 'E',
        b'\xca' : 'E',
        b'\xcb' : 'E',
        b'\xcc' : 'I',
        b'\xcd' : 'I',
        b'\xce' : 'I',
        b'\xcf' : 'I',
        b'\xd0' : 'D',
        b'\xd1' : 'N',
        b'\xd2' : 'O',
        b'\xd3' : 'O',
        b'\xd4' : 'O',
        b'\xd5' : 'O',
        b'\xd6' : 'O',
        b'\xd7' : '*',
        b'\xd8' : 'O',
        b'\xd9' : 'U',
        b'\xda' : 'U',
        b'\xdb' : 'U',
        b'\xdc' : 'U',
        b'\xdd' : 'Y',
        b'\xde' : 'b',
        b'\xdf' : 'B',
        b'\xe0' : 'a',
        b'\xe1' : 'a',
        b'\xe2' : 'a',
        b'\xe3' : 'a',
        b'\xe4' : 'a',
        b'\xe5' : 'a',
        b'\xe6' : 'ae',
        b'\xe7' : 'c',
        b'\xe8' : 'e',
        b'\xe9' : 'e',
        b'\xea' : 'e',
        b'\xeb' : 'e',
        b'\xec' : 'i',
        b'\xed' : 'i',
        b'\xee' : 'i',
        b'\xef' : 'i',
        b'\xf0' : 'o',
        b'\xf1' : 'n',
        b'\xf2' : 'o',
        b'\xf3' : 'o',
        b'\xf4' : 'o',
        b'\xf5' : 'o',
        b'\xf6' : 'o',
        b'\xf7' : '/',
        b'\xf8' : 'o',
        b'\xf9' : 'u',
        b'\xfa' : 'u',
        b'\xfb' : 'u',
        b'\xfc' : 'u',
        b'\xfd' : 'y',
        b'\xfe' : 'b',
        b'\xff' : 'y',
        }

    
    
    
    
    
    WINDOWS_1252_TO_UTF8 = {
        0x80 : b'\xe2\x82\xac', 
        0x82 : b'\xe2\x80\x9a', 
        0x83 : b'\xc6\x92',     
        0x84 : b'\xe2\x80\x9e', 
        0x85 : b'\xe2\x80\xa6', 
        0x86 : b'\xe2\x80\xa0', 
        0x87 : b'\xe2\x80\xa1', 
        0x88 : b'\xcb\x86',     
        0x89 : b'\xe2\x80\xb0', 
        0x8a : b'\xc5\xa0',     
        0x8b : b'\xe2\x80\xb9', 
        0x8c : b'\xc5\x92',     
        0x8e : b'\xc5\xbd',     
        0x91 : b'\xe2\x80\x98', 
        0x92 : b'\xe2\x80\x99', 
        0x93 : b'\xe2\x80\x9c', 
        0x94 : b'\xe2\x80\x9d', 
        0x95 : b'\xe2\x80\xa2', 
        0x96 : b'\xe2\x80\x93', 
        0x97 : b'\xe2\x80\x94', 
        0x98 : b'\xcb\x9c',     
        0x99 : b'\xe2\x84\xa2', 
        0x9a : b'\xc5\xa1',     
        0x9b : b'\xe2\x80\xba', 
        0x9c : b'\xc5\x93',     
        0x9e : b'\xc5\xbe',     
        0x9f : b'\xc5\xb8',     
        0xa0 : b'\xc2\xa0',     
        0xa1 : b'\xc2\xa1',     
        0xa2 : b'\xc2\xa2',     
        0xa3 : b'\xc2\xa3',     
        0xa4 : b'\xc2\xa4',     
        0xa5 : b'\xc2\xa5',     
        0xa6 : b'\xc2\xa6',     
        0xa7 : b'\xc2\xa7',     
        0xa8 : b'\xc2\xa8',     
        0xa9 : b'\xc2\xa9',     
        0xaa : b'\xc2\xaa',     
        0xab : b'\xc2\xab',     
        0xac : b'\xc2\xac',     
        0xad : b'\xc2\xad',     
        0xae : b'\xc2\xae',     
        0xaf : b'\xc2\xaf',     
        0xb0 : b'\xc2\xb0',     
        0xb1 : b'\xc2\xb1',     
        0xb2 : b'\xc2\xb2',     
        0xb3 : b'\xc2\xb3',     
        0xb4 : b'\xc2\xb4',     
        0xb5 : b'\xc2\xb5',     
        0xb6 : b'\xc2\xb6',     
        0xb7 : b'\xc2\xb7',     
        0xb8 : b'\xc2\xb8',     
        0xb9 : b'\xc2\xb9',     
        0xba : b'\xc2\xba',     
        0xbb : b'\xc2\xbb',     
        0xbc : b'\xc2\xbc',     
        0xbd : b'\xc2\xbd',     
        0xbe : b'\xc2\xbe',     
        0xbf : b'\xc2\xbf',     
        0xc0 : b'\xc3\x80',     
        0xc1 : b'\xc3\x81',     
        0xc2 : b'\xc3\x82',     
        0xc3 : b'\xc3\x83',     
        0xc4 : b'\xc3\x84',     
        0xc5 : b'\xc3\x85',     
        0xc6 : b'\xc3\x86',     
        0xc7 : b'\xc3\x87',     
        0xc8 : b'\xc3\x88',     
        0xc9 : b'\xc3\x89',     
        0xca : b'\xc3\x8a',     
        0xcb : b'\xc3\x8b',     
        0xcc : b'\xc3\x8c',     
        0xcd : b'\xc3\x8d',     
        0xce : b'\xc3\x8e',     
        0xcf : b'\xc3\x8f',     
        0xd0 : b'\xc3\x90',     
        0xd1 : b'\xc3\x91',     
        0xd2 : b'\xc3\x92',     
        0xd3 : b'\xc3\x93',     
        0xd4 : b'\xc3\x94',     
        0xd5 : b'\xc3\x95',     
        0xd6 : b'\xc3\x96',     
        0xd7 : b'\xc3\x97',     
        0xd8 : b'\xc3\x98',     
        0xd9 : b'\xc3\x99',     
        0xda : b'\xc3\x9a',     
        0xdb : b'\xc3\x9b',     
        0xdc : b'\xc3\x9c',     
        0xdd : b'\xc3\x9d',     
        0xde : b'\xc3\x9e',     
        0xdf : b'\xc3\x9f',     
        0xe0 : b'\xc3\xa0',     
        0xe1 : b'\xa1',     
        0xe2 : b'\xc3\xa2',     
        0xe3 : b'\xc3\xa3',     
        0xe4 : b'\xc3\xa4',     
        0xe5 : b'\xc3\xa5',     
        0xe6 : b'\xc3\xa6',     
        0xe7 : b'\xc3\xa7',     
        0xe8 : b'\xc3\xa8',     
        0xe9 : b'\xc3\xa9',     
        0xea : b'\xc3\xaa',     
        0xeb : b'\xc3\xab',     
        0xec : b'\xc3\xac',     
        0xed : b'\xc3\xad',     
        0xee : b'\xc3\xae',     
        0xef : b'\xc3\xaf',     
        0xf0 : b'\xc3\xb0',     
        0xf1 : b'\xc3\xb1',     
        0xf2 : b'\xc3\xb2',     
        0xf3 : b'\xc3\xb3',     
        0xf4 : b'\xc3\xb4',     
        0xf5 : b'\xc3\xb5',     
        0xf6 : b'\xc3\xb6',     
        0xf7 : b'\xc3\xb7',     
        0xf8 : b'\xc3\xb8',     
        0xf9 : b'\xc3\xb9',     
        0xfa : b'\xc3\xba',     
        0xfb : b'\xc3\xbb',     
        0xfc : b'\xc3\xbc',     
        0xfd : b'\xc3\xbd',     
        0xfe : b'\xc3\xbe',     
        }

    MULTIBYTE_MARKERS_AND_SIZES = [
        (0xc2, 0xdf, 2), 
        (0xe0, 0xef, 3), 
        (0xf0, 0xf4, 4), 
        ]

    FIRST_MULTIBYTE_MARKER = MULTIBYTE_MARKERS_AND_SIZES[0][0]
    LAST_MULTIBYTE_MARKER = MULTIBYTE_MARKERS_AND_SIZES[-1][1]

    @classmethod
    def detwingle(cls, in_bytes, main_encoding="utf8",
                  embedded_encoding="windows-1252"):
        
        if embedded_encoding.replace('_', '-').lower() not in (
            'windows-1252', 'windows_1252'):
            raise NotImplementedError(
                "Windows-1252 and ISO-8859-1 are the only currently supported "
                "embedded encodings.")

        if main_encoding.lower() not in ('utf8', 'utf-8'):
            raise NotImplementedError(
                "UTF-8 is the only currently supported main encoding.")

        byte_chunks = []

        chunk_start = 0
        pos = 0
        while pos < len(in_bytes):
            byte = in_bytes[pos]
            if not isinstance(byte, int):
                
                byte = ord(byte)
            if (byte >= cls.FIRST_MULTIBYTE_MARKER
                and byte <= cls.LAST_MULTIBYTE_MARKER):
                
                
                for start, end, size in cls.MULTIBYTE_MARKERS_AND_SIZES:
                    if byte >= start and byte <= end:
                        pos += size
                        break
            elif byte >= 0x80 and byte in cls.WINDOWS_1252_TO_UTF8:
                
                
                byte_chunks.append(in_bytes[chunk_start:pos])

                
                
                byte_chunks.append(cls.WINDOWS_1252_TO_UTF8[byte])
                pos += 1
                chunk_start = pos
            else:
                
                pos += 1
        if chunk_start == 0:
            
            return in_bytes
        else:
            
            byte_chunks.append(in_bytes[chunk_start:])
        return b''.join(byte_chunks)

