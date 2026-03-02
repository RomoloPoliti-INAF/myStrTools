import re


_WORD_PATTERN = re.compile(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|\d+")


def split_words(text: str) -> list[str]:
    normalized = re.sub(r"[^0-9A-Za-z]+", " ", text.strip())
    if not normalized:
        return []

    words: list[str] = []
    for token in normalized.split():
        words.extend(_WORD_PATTERN.findall(token))
    return words