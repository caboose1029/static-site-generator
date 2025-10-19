from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: str, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node) -> bool:
        return (
            self.text
            == node.text & self.text_type
            == node.text_type & self.url
            == node.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
