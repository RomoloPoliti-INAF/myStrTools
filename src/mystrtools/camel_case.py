from mystrtools._word_split import split_words

def camel_case(text: str) -> str:
    """
    Converts a given string to camelCase.

    The function transforms a string by removing underscores or hyphens,
    capitalizing the first letter of each word except the first one,
    and then joining them together to form a camelCase string.

    Args:
        text (str): The input string, typically in snake_case or kebab-case.

    Returns:
        str: The converted string in camelCase.

    Example:
        >>> camel_case('hello_world')
        'helloWorld'
        >>> camel_case('hello-world')
        'helloWorld'
    """
    words = split_words(text)
    if not words:
        return ""

    first_word = words[0].lower()
    tail = "".join(word.lower().capitalize() for word in words[1:])
    return f"{first_word}{tail}"