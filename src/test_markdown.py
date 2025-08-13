import unittest

from markdown import BlockType, markdown_to_blocks, block_to_block_type, markdown_to_html_node

class TestMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        header = block_to_block_type("# Heading")
        self.assertEqual(header, BlockType.HEADING)

        code = block_to_block_type("```\ncode block\n```")
        self.assertEqual(code, BlockType.CODE)

        quote = block_to_block_type("> quote 1.\n> quote 2.")
        self.assertEqual(quote, BlockType.QUOTE)

        ulist = block_to_block_type("- list 1\n- list 2")
        self.assertEqual(ulist, BlockType.ULIST)

        olist = block_to_block_type("1. list\n2. list")
        self.assertEqual(olist, BlockType.OLIST)

        paragraph = block_to_block_type("regular text")
        self.assertEqual(paragraph, BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )