import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("h1", "Some title", None, {"id": "title", "title": "Yes its a title?"})
        self.assertEqual(node.props_to_method(), ' id="title" title="Yes its a title?"')
    
    def test_value_children(self):
        node = HTMLNode("div", "Something", None)
        node2 = HTMLNode("div", None, "Children", None)
        self.assertNotEqual(node, node2)

    def test_prompt_no_value(self):
        node = HTMLNode("div", "My Div!", None, {"id": None, "alt": "Alt Text"})
        self.assertNotEqual(node.props_to_method(), ' id= alt="Alt Text"')