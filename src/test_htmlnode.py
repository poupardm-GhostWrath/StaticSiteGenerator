import unittest

from htmlnode import *

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
    """

    """
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    """
    def test_eq(self):
        testCase = {
            TextType.TEXT:["This is a text node"],
            TextType.BOLD:["This is a bold node"],
            TextType.ITALIC:["This is an italic node"],
            TextType.CODE:["This is a code node"],
            TextType.LINK:["This is a link node", {"href":"https://www.boot.dev"}],
            TextType.IMAGE:["This is an image node", {"src":"~/banana.png"}],
        }
        testCaseOutput = {
            TextType.TEXT:[None, "This is a text node"],
            TextType.BOLD:["b", "This is a bold node"],
            TextType.ITALIC:["i", "This is an italic node"],
            TextType.CODE:["code", "This is a code node"],
            TextType.LINK:["a", "This is a link node"],
            TextType.IMAGE:["img", "This is an image node"],
        }
        for test in testCase:
            node = None
            if len(testCase[test]) < 2:
                node = TextNode(testCase[test][0], test)
            else:
                node = TextNode(testCase[test][0], test, testCase[test][1])
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, testCaseOutput[test][0])
            self.assertEqual(html_node.value, testCaseOutput[test][1])

    def test_textToNodes(self):
        testCaseOutput = [
            TextNode("This is **text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        testCase = "This is **text with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        output = text_to_textnodes(testCase)
        self.assertEqual(output, testCaseOutput)