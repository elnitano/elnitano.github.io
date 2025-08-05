import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_false(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_image_false(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node2", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_italic_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode(None, TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()