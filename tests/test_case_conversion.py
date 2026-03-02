import pytest

from mystrtools import (
    camel_to_kebab,
    camel_to_pascal,
    camel_to_snake,
    camel_to_space,
    camel_case,
    camel_to_spaces,
    convert_case,
    kebab_case,
    kebab_to_camel,
    kebab_to_pascal,
    kebab_to_snake,
    kebab_to_space,
    pascal_case,
    pascal_to_camel,
    pascal_to_kebab,
    pascal_to_snake,
    pascal_to_space,
    snake_to_camel,
    snake_to_kebab,
    snake_to_pascal,
    snake_to_space,
    space_to_camel,
    space_to_kebab,
    space_to_pascal,
    space_to_snake,
    snake_case,
)


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("hello_world", "helloWorld"),
        ("hello-world", "helloWorld"),
        ("HelloWorld", "helloWorld"),
        ("JSONParser", "jsonParser"),
        ("convert2JSON_value", "convert2JsonValue"),
        ("  multiple   separators---here__ok ", "multipleSeparatorsHereOk"),
        ("", ""),
    ],
)
def test_camel_case(source: str, expected: str) -> None:
    assert camel_case(source) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("hello_world", "HelloWorld"),
        ("hello-world", "HelloWorld"),
        ("helloWorld", "HelloWorld"),
        ("JSONParser", "JsonParser"),
        ("convert2JSON_value", "Convert2JsonValue"),
        ("", ""),
    ],
)
def test_pascal_case(source: str, expected: str) -> None:
    assert pascal_case(source) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("helloWorld", "hello_world"),
        ("HelloWorld", "hello_world"),
        ("JSONParser", "json_parser"),
        ("convert2JSON_value", "convert_2_json_value"),
        ("already_snake_case", "already_snake_case"),
        ("", ""),
    ],
)
def test_snake_case(source: str, expected: str) -> None:
    assert snake_case(source) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("helloWorld", "hello-world"),
        ("HelloWorld", "hello-world"),
        ("JSONParser", "json-parser"),
        ("convert2JSON_value", "convert-2-json-value"),
        ("already-kebab-case", "already-kebab-case"),
        ("", ""),
    ],
)
def test_kebab_case(source: str, expected: str) -> None:
    assert kebab_case(source) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("CamelCaseString", "camel case string"),
        ("camelCaseString", "camel case string"),
        ("JSONParser", "json parser"),
        ("already_snake_case", "already snake case"),
        ("convert2JSON_value", "convert 2 json value"),
        ("", ""),
    ],
)
def test_camel_to_spaces(source: str, expected: str) -> None:
    assert camel_to_spaces(source) == expected


@pytest.mark.parametrize(
    ("source", "target", "expected"),
    [
        ("hello_world", "camel", "helloWorld"),
        ("hello_world", "pascal", "HelloWorld"),
        ("helloWorld", "snake", "hello_world"),
        ("HelloWorld", "kebab", "hello-world"),
        ("JSONParser", "space", "json parser"),
    ],
)
def test_convert_case(source: str, target: str, expected: str) -> None:
    assert convert_case(source, target) == expected #type: ignore


def test_convert_case_invalid_target() -> None:
    with pytest.raises(ValueError, match="Unsupported format"):
        convert_case("helloWorld", "invalid") #type: ignore


@pytest.mark.parametrize(
    ("func", "source", "expected"),
    [
        (camel_to_pascal, "hello_world", "HelloWorld"),
        (camel_to_snake, "helloWorld", "hello_world"),
        (camel_to_kebab, "helloWorld", "hello-world"),
        (camel_to_space, "helloWorld", "hello world"),
        (snake_to_camel, "hello_world", "helloWorld"),
        (kebab_to_snake, "hello-world", "hello_world"),
        (space_to_pascal, "hello world", "HelloWorld"),
    ],
)
def test_explicit_transition_wrappers(func, source: str, expected: str) -> None:
    assert func(source) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        (
            "JSONParser",
            {
                "camel": "jsonParser",
                "pascal": "JsonParser",
                "snake": "json_parser",
                "kebab": "json-parser",
                "space": "json parser",
            },
        ),
        (
            "convert2JSON_value",
            {
                "camel": "convert2JsonValue",
                "pascal": "Convert2JsonValue",
                "snake": "convert_2_json_value",
                "kebab": "convert-2-json-value",
                "space": "convert 2 json value",
            },
        ),
        (
            "  multiple---separators__here  ",
            {
                "camel": "multipleSeparatorsHere",
                "pascal": "MultipleSeparatorsHere",
                "snake": "multiple_separators_here",
                "kebab": "multiple-separators-here",
                "space": "multiple separators here",
            },
        ),
        (
            "",
            {
                "camel": "",
                "pascal": "",
                "snake": "",
                "kebab": "",
                "space": "",
            },
        ),
    ],
)
def test_edge_case_conversion_matrix(source: str, expected: dict[str, str]) -> None:
    for target, target_value in expected.items():
        assert convert_case(source, target) == target_value #type: ignore


@pytest.mark.parametrize(
    ("func", "source", "expected"),
    [
        (pascal_to_camel, "HelloWorld", "helloWorld"),
        (pascal_to_snake, "HelloWorld", "hello_world"),
        (pascal_to_kebab, "HelloWorld", "hello-world"),
        (pascal_to_space, "HelloWorld", "hello world"),
        (snake_to_pascal, "hello_world", "HelloWorld"),
        (snake_to_kebab, "hello_world", "hello-world"),
        (snake_to_space, "hello_world", "hello world"),
        (kebab_to_camel, "hello-world", "helloWorld"),
        (kebab_to_pascal, "hello-world", "HelloWorld"),
        (kebab_to_space, "hello-world", "hello world"),
        (space_to_camel, "hello world", "helloWorld"),
        (space_to_snake, "hello world", "hello_world"),
        (space_to_kebab, "hello world", "hello-world"),
    ],
)
def test_remaining_transition_wrappers(func, source: str, expected: str) -> None:
    assert func(source) == expected
