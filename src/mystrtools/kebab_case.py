from mystrtools._word_split import split_words


def kebab_case(text: str) -> str:
    """
    Converts a given string to kebab-case.

    Args:
        text (str): Input string in any common case style.

    Returns:
        str: Converted string in kebab-case.
    """
    return "-".join(word.lower() for word in split_words(text))