import unittest

from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
    def test_images(self):
        testCase = {
            1 : "This is text with a single image ![Monkey](https://monkey.banana)",
            2 : "This is text with multiple images ![Banana](https://banana.monkey) ![Monkey](https://monkey.banana)"
        }
        testOutput = {
            1 : [("Monkey", "https://monkey.banana")],
            2 : [("Banana", "https://banana.monkey"), ("Monkey", "https://monkey.banana")]
        }
        for test in testCase:
            matches = extract_markdown_images(testCase[test])
            self.assertEqual(testOutput[test], matches)
        pass

    def test_links(self):
        testCase = {
            1 : "This is text with a single links [Monkey](https://monkey.banana)",
            2 : "This is text with multiple links [Banana](https://banana.monkey) [Monkey](https://monkey.banana)"
        }
        testOutput = {
            1 : [("Monkey", "https://monkey.banana")],
            2 : [("Banana", "https://banana.monkey"), ("Monkey", "https://monkey.banana")]
        }
        for test in testCase:
            matches = extract_markdown_links(testCase[test])
            self.assertEqual(testOutput[test], matches)
        pass