import unittest
from markdown_to_html_node import markdown_to_html_node
from HTMLNode import HTMLNODE

class TestParagraphs(unittest.TestCase):
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
    def test_unordered_listblock(self):
        md = """
        I went to the market this morning and bought some fruit.
The weather was nice so I walked instead of driving.

- apples
- bananas
- oranges
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>I went to the market this morning and bought some fruit. The weather was nice so I walked instead of driving.</p><ul><li>apples</li><li>bananas</li><li>oranges</li></ul></div>"
            )
    def test_list_then_paragraph(self):
        md = """
- bread
- milk
- eggs

These were the last things on my shopping list.
I was relieved to finally head home.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>bread</li><li>milk</li><li>eggs</li></ul><p>These were the last things on my shopping list. I was relieved to finally head home.</p></div>"
        )
    def test_paragraph_list_paragraph(self):
        md = """
Making coffee in the morning is a small ritual I enjoy.
It helps me wake up before starting work.

1. Boil water
2. Grind beans
3. Brew coffee

Once the coffee is ready, the day finally feels like it can begin.
Sometimes I just sit quietly and enjoy the smell.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Making coffee in the morning is a small ritual I enjoy. It helps me wake up before starting work.</p><ol><li>Boil water</li><li>Grind beans</li><li>Brew coffee</li></ol><p>Once the coffee is ready, the day finally feels like it can begin. Sometimes I just sit quietly and enjoy the smell.</p></div>"
        )
    def test_edgecase(self):
        md = """
This recipe is simple but requires careful timing.
Follow each step in order so nothing burns.

1. Preheat the oven
2. Mix the batter
10. Pour into pan
11. Bake for thirty minutes

Once it finishes baking, let it cool before slicing.
Otherwise the cake will fall apart.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This recipe is simple but requires careful timing. Follow each step in order so nothing burns.</p><ol><li>Preheat the oven</li><li>Mix the batter</li><li>Pour into pan</li><li>Bake for thirty minutes</li></ol><p>Once it finishes baking, let it cool before slicing. Otherwise the cake will fall apart.</p></div>"
        )