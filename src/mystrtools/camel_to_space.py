from mystrtools._word_split import split_words

def camel_to_spaces(text: str) -> str:
    """
    Converts CamelCase or mixedCase into space-separated lowercase words.
    Example: "CamelCaseString" -> "camel case string"
    """
    return " ".join(word.lower() for word in split_words(text))