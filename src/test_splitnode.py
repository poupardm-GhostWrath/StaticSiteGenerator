import unittest

from splitnode import *
from textnode import *

class TestSplitNode(unittest.TestCase):
    def test_splitnode(self):
        testCase = {
            TextType.CODE:["Text with a 'code block' word"],
            TextType.BOLD:["Text with a **bold** word"],
            TextType.ITALIC:["Text with a _italic_ word"],
        }
        testDelimiter = {
            TextType.CODE:"'",
            TextType.BOLD:"**",
            TextType.ITALIC:"_",
        }
        testCaseOutput = {
            TextType.CODE:[
                TextNode("Text with a ", TextType.TEXT), 
                TextNode("code block", TextType.CODE), 
                TextNode(" word", TextType.TEXT)
            ],
            TextType.BOLD:[
                TextNode("Text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ],
            TextType.ITALIC:[
                TextNode("Text with a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT)
            ],
        }
        for test in testCase:
            node = TextNode(testCase[test][0], TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], testDelimiter[test], test)
            self.assertEqual(testCaseOutput[test], new_nodes)

        node = TextNode("Text with wrong TextType", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual([node], new_nodes)
        pass

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) banana",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        """
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" banana", TextType.TEXT)
            ],
            new_nodes,
        )
        """

    def test_split_links(self):
        node = TextNode(
            "This is text with a [to boot dev](https://www.boot.dev) and another [to google](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "to google", TextType.LINK, "https://www.google.com"
                ),
            ],
            new_nodes,
        )