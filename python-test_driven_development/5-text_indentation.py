#!/usr/bin/python3
"""Module that provides a function to print formatted text."""


def text_indentation(text):
    """Print text with two new lines after ., ? and : characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""

    if buffer.strip():
        print(buffer.strip(), end="")
