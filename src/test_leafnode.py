import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_o(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_no_tag(self):
        node = LeafNode(None, "No tag!")
        self.assertEqual(node.to_html(), "No tag!")

    def test_leaf_link(self):
        node = LeafNode("a", "Link", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Link</a>')