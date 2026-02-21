import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    """
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

    """

    def test_leafNode(self):
        testCase = {
            "h1" : ["Heading 1"],
            "p" : ["Paragraph"],
            "b" : ["Bold"],
            "i" : ["Italic"],
            "blockquote" : ["Quote"],
            "code" : ["Code"],
            "a" : ["Boot.dev", {"href" : "https://www.boot.dev"}],
            "img" : ["Image of Banana", {"src" : "~/banana.png"}],
        }
        testCaseOutput = {
            "h1" : "<h1>Heading 1</h1>",
            "p" : "<p>Paragraph</p>",
            "b" : "<b>Bold</b>",
            "i" : "<i>Italic</i>",
            "blockquote" : "<blockquote>Quote</blockquote>",
            "code" : "<code>Code</code>",
            "a" : '<a href="https://www.boot.dev">Boot.dev</a>',
            "img": '<img src="~/banana.png" alt="Image of Banana" />',
        }
        for test in testCase:
            node = None
            if len(testCase[test]) < 2:
                node = LeafNode(test, testCase[test][0])
            else:
                node = LeafNode(test, testCase[test][0], testCase[test][1])
            self.assertEqual(node.to_html(), testCaseOutput[test])