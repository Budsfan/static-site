from textnode import TextType, TextNode

def main():
    node = TextNode("Here is some text", TextType.LINK, "https://www.boot.dev")
    print(node)

main()