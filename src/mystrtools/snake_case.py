from mystrtools._word_split import split_words

def snake_case(text: str) -> str:
    """
    Converts a given string to snake_case.

    The function transforms a camelCase or PascalCase string to snake_case,
    replacing capital letters with underscores followed by the lowercase equivalent.

    Args:
        text (str): The input string, typically in camelCase or PascalCase.

    Returns:
        str: The converted string in snake_case.

    Example:
        >>> snake_case('helloWorld')
        'hello_world'
        >>> snake_case('HelloWorld')
        'hello_world'
    """
    return "_".join(word.lower() for word in split_words(text))