# mystrtools

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue?style=plastic&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/version-0.1.0-blueviolet?style=plastic)
![Tests](https://img.shields.io/badge/tests-61%20passed-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
<!-- [![DOI](https://zenodo.org/badge/1167626806.svg)](https://doi.org/10.5281/zenodo.18832548) -->




Small Python utilities to convert strings across common naming styles.

Supported styles:
- `camelCase`
- `PascalCase`
- `snake_case`
- `kebab-case`
- `space separated words`

## Citation

If you use `mystrtools`, please cite it using [CITATION.cff](CITATION.cff).

<!-- DOI: [10.5281/zenodo.18832548](https://doi.org/10.5281/zenodo.18832548) -->

## Installation

With Poetry:

```bash
poetry install
```

Or as a package dependency:

```bash
pip install mystrtools
```

## Quick Start

```python
from mystrtools import camel_case, snake_case, kebab_case, pascal_case, camel_to_spaces

camel_case("hello_world")         # "helloWorld"
pascal_case("hello_world")        # "HelloWorld"
snake_case("HelloWorld")          # "hello_world"
kebab_case("HelloWorld")          # "hello-world"
camel_to_spaces("JSONParser")     # "json parser"
```

## Core Methods

### `camel_case(text: str) -> str`
Converts any supported input style to `camelCase`.

### `pascal_case(text: str) -> str`
Converts any supported input style to `PascalCase`.

### `snake_case(text: str) -> str`
Converts any supported input style to `snake_case`.

### `kebab_case(text: str) -> str`
Converts any supported input style to `kebab-case`.

### `camel_to_spaces(text: str) -> str`
Converts any supported input style to lowercase space-separated words.

## Generic Cross-Format Conversion

### `convert_case(text: str, to_format: CaseFormat) -> str`

`CaseFormat` accepted values:
- `"camel"`
- `"pascal"`
- `"snake"`
- `"kebab"`
- `"space"`

Example:

```python
from mystrtools import convert_case

convert_case("hello_world", "camel")   # "helloWorld"
convert_case("JSONParser", "snake")    # "json_parser"
convert_case("convert2JSON", "space")  # "convert 2 json"
```

If `to_format` is not valid, `convert_case` raises `ValueError`.

## Explicit Transition Methods

All direct transitions are also available as dedicated helper functions.

From camel:
- `camel_to_pascal`
- `camel_to_snake`
- `camel_to_kebab`
- `camel_to_space`

From pascal:
- `pascal_to_camel`
- `pascal_to_snake`
- `pascal_to_kebab`
- `pascal_to_space`

From snake:
- `snake_to_camel`
- `snake_to_pascal`
- `snake_to_kebab`
- `snake_to_space`

From kebab:
- `kebab_to_camel`
- `kebab_to_pascal`
- `kebab_to_snake`
- `kebab_to_space`

From space-separated:
- `space_to_camel`
- `space_to_pascal`
- `space_to_snake`
- `space_to_kebab`

Example:

```python
from mystrtools import snake_to_camel, kebab_to_snake, space_to_pascal

snake_to_camel("hello_world")  # "helloWorld"
kebab_to_snake("hello-world")  # "hello_world"
space_to_pascal("hello world") # "HelloWorld"
```

## Compatibility Matrix

The table below shows supported conversions between source and target styles.

| From \ To | camel | pascal | snake | kebab | space |
|---|---|---|---|---|---|
| camel | `camel_case` / `convert_case(..., "camel")` | `camel_to_pascal` | `camel_to_snake` | `camel_to_kebab` | `camel_to_space` |
| pascal | `pascal_to_camel` | `pascal_case` / `convert_case(..., "pascal")` | `pascal_to_snake` | `pascal_to_kebab` | `pascal_to_space` |
| snake | `snake_to_camel` | `snake_to_pascal` | `snake_case` / `convert_case(..., "snake")` | `snake_to_kebab` | `snake_to_space` |
| kebab | `kebab_to_camel` | `kebab_to_pascal` | `kebab_to_snake` | `kebab_case` / `convert_case(..., "kebab")` | `kebab_to_space` |
| space | `space_to_camel` | `space_to_pascal` | `space_to_snake` | `space_to_kebab` | `camel_to_spaces` / `convert_case(..., "space")` |

Note: all methods share the same normalization behavior (acronyms, mixed separators, numbers, and blank input handling).

Quick examples by source format:

```python
from mystrtools import convert_case

convert_case("helloWorld", "snake")   # camel -> snake: "hello_world"
convert_case("HelloWorld", "kebab")  # pascal -> kebab: "hello-world"
convert_case("hello_world", "pascal")# snake -> pascal: "HelloWorld"
convert_case("hello-world", "camel") # kebab -> camel: "helloWorld"
convert_case("hello world", "snake") # space -> snake: "hello_world"
```

### Edge-Case Conversion Matrix

Reference outputs for common tricky inputs:

| Input | camel | pascal | snake | kebab | space |
|---|---|---|---|---|---|
| `JSONParser` | `jsonParser` | `JsonParser` | `json_parser` | `json-parser` | `json parser` |
| `convert2JSON_value` | `convert2JsonValue` | `Convert2JsonValue` | `convert_2_json_value` | `convert-2-json-value` | `convert 2 json value` |
| `  multiple---separators__here  ` | `multipleSeparatorsHere` | `MultipleSeparatorsHere` | `multiple_separators_here` | `multiple-separators-here` | `multiple separators here` |
| `` (empty string) | `` | `` | `` | `` | `` |

## Normalization Rules

The library applies the same normalization logic across all methods:
- Handles mixed separators (`_`, `-`, spaces, punctuation)
- Splits acronyms consistently (`JSONParser` -> `json parser`)
- Keeps numeric blocks (`version2Update` -> `version_2_update` in snake)
- Returns an empty string for empty/blank input

## Development

Run tests:

```bash
pytest -q
```

## Testing & Coverage

The project is configured to run tests with coverage reporting.

Run full test suite with coverage:

```bash
pytest
```

Generated artifacts:
- Terminal coverage summary
- HTML report in `coverage/coverage_html`
- XML report in `coverage/coverage.xml`
- JSON report in `coverage/coverage.json`

Example result:

```text
61 passed
TOTAL ... 100%
```
