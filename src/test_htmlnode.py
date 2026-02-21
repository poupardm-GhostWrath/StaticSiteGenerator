import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_emptyProps(self):
        node = HTMLNode()
        print(node)
        self.assertEqual(node.props_to_html(), "")
    
    def test_props(self):
        node = HTMLNode("p", "Banana", None, {"href" : "https://www.boot.dev", "target" : "_blank"})
        print(node)
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

    def test_repr(self):
        node = HTMLNode("p", "Monkey", None, {"href" : "https://www.google.com", "target" : "_blank"})
        print(node)
        pass