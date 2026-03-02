from typing import Literal

from mystrtools.camel_case import camel_case
from mystrtools.camel_to_space import camel_to_spaces
from mystrtools.kebab_case import kebab_case
from mystrtools.pascal_case import pascal_case
from mystrtools.snake_case import snake_case

CaseFormat = Literal["camel", "pascal", "snake", "kebab", "space"]


def convert_case(text: str, to_format: CaseFormat) -> str:
    converters = {
        "camel": camel_case,
        "pascal": pascal_case,
        "snake": snake_case,
        "kebab": kebab_case,
        "space": camel_to_spaces,
    }
    try:
        return converters[to_format](text)
    except KeyError as exc:
        expected = ", ".join(converters)
        raise ValueError(f"Unsupported format: {to_format}. Use one of: {expected}") from exc


def camel_to_pascal(text: str) -> str:
    return pascal_case(text)


def camel_to_snake(text: str) -> str:
    return snake_case(text)


def camel_to_kebab(text: str) -> str:
    return kebab_case(text)


def camel_to_space(text: str) -> str:
    return camel_to_spaces(text)


def pascal_to_camel(text: str) -> str:
    return camel_case(text)


def pascal_to_snake(text: str) -> str:
    return snake_case(text)


def pascal_to_kebab(text: str) -> str:
    return kebab_case(text)


def pascal_to_space(text: str) -> str:
    return camel_to_spaces(text)


def snake_to_camel(text: str) -> str:
    return camel_case(text)


def snake_to_pascal(text: str) -> str:
    return pascal_case(text)


def snake_to_kebab(text: str) -> str:
    return kebab_case(text)


def snake_to_space(text: str) -> str:
    return camel_to_spaces(text)


def kebab_to_camel(text: str) -> str:
    return camel_case(text)


def kebab_to_pascal(text: str) -> str:
    return pascal_case(text)


def kebab_to_snake(text: str) -> str:
    return snake_case(text)


def kebab_to_space(text: str) -> str:
    return camel_to_spaces(text)


def space_to_camel(text: str) -> str:
    return camel_case(text)


def space_to_pascal(text: str) -> str:
    return pascal_case(text)


def space_to_snake(text: str) -> str:
    return snake_case(text)


def space_to_kebab(text: str) -> str:
    return kebab_case(text)


__all__ = [
    "CaseFormat",
    "convert_case",
    "camel_to_pascal",
    "camel_to_snake",
    "camel_to_kebab",
    "camel_to_space",
    "pascal_to_camel",
    "pascal_to_snake",
    "pascal_to_kebab",
    "pascal_to_space",
    "snake_to_camel",
    "snake_to_pascal",
    "snake_to_kebab",
    "snake_to_space",
    "kebab_to_camel",
    "kebab_to_pascal",
    "kebab_to_snake",
    "kebab_to_space",
    "space_to_camel",
    "space_to_pascal",
    "space_to_snake",
    "space_to_kebab",
]