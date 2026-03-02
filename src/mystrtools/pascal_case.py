from mystrtools._word_split import split_words


def pascal_case(text: str) -> str:
    """
    Converts a given string to PascalCase.

    Args:
        text (str): Input string in any common case style.

    Returns:
        str: Converted string in PascalCase.
    """
    return "".join(word.lower().capitalize() for word in split_words(text))