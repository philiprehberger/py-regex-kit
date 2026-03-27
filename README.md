# philiprehberger-regex-kit

[![Tests](https://github.com/philiprehberger/py-regex-kit/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-regex-kit/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-regex-kit.svg)](https://pypi.org/project/philiprehberger-regex-kit/)
[![License](https://img.shields.io/github/license/philiprehberger/py-regex-kit)](LICENSE)
[![Sponsor](https://img.shields.io/badge/sponsor-GitHub%20Sponsors-ec6cb9)](https://github.com/sponsors/philiprehberger)

Pre-built, tested regex patterns for common data formats.

## Installation

```bash
pip install philiprehberger-regex-kit
```

## Usage

```python
from philiprehberger_regex_kit import patterns, extract, is_match

# Use compiled patterns directly
if patterns.EMAIL.fullmatch("user@example.com"):
    print("Valid email")

# Quick validation by name
is_match("ip_v4", "192.168.1.1")  # True
is_match("uuid", "not-a-uuid")    # False
```

### Extracting Matches

```python
from philiprehberger_regex_kit import extract

text = "Contact alice@example.com or visit https://example.com"

extract.emails(text)  # ["alice@example.com"]
extract.urls(text)    # ["https://example.com"]
```

### Available Patterns

```python
from philiprehberger_regex_kit import patterns

patterns.EMAIL        # Email addresses
patterns.URL          # HTTP/HTTPS URLs
patterns.IP_V4        # IPv4 addresses
patterns.IP_V6        # IPv6 addresses (full form)
patterns.PHONE        # Phone numbers
patterns.UUID         # UUIDs
patterns.HEX_COLOR    # Hex color codes (#fff, #ff00aa)
patterns.DATE_ISO     # ISO dates (YYYY-MM-DD)
patterns.TIME_24H     # 24-hour time (HH:MM or HH:MM:SS)
patterns.CREDIT_CARD  # Credit card numbers
patterns.MAC_ADDRESS  # MAC addresses
patterns.DOMAIN       # Domain names
```

## API

### `patterns`

| Attribute | Description |
|-----------|-------------|
| `patterns.EMAIL` | Compiled pattern for email addresses |
| `patterns.URL` | Compiled pattern for HTTP/HTTPS URLs |
| `patterns.IP_V4` | Compiled pattern for IPv4 addresses |
| `patterns.IP_V6` | Compiled pattern for IPv6 addresses |
| `patterns.PHONE` | Compiled pattern for phone numbers |
| `patterns.UUID` | Compiled pattern for UUIDs |
| `patterns.HEX_COLOR` | Compiled pattern for hex color codes |
| `patterns.DATE_ISO` | Compiled pattern for ISO 8601 dates |
| `patterns.TIME_24H` | Compiled pattern for 24-hour time |
| `patterns.CREDIT_CARD` | Compiled pattern for credit card numbers |
| `patterns.MAC_ADDRESS` | Compiled pattern for MAC addresses |
| `patterns.DOMAIN` | Compiled pattern for domain names |

### `extract`

| Method | Description |
|--------|-------------|
| `extract.emails(text)` | Extract all email addresses |
| `extract.urls(text)` | Extract all URLs |
| `extract.phones(text)` | Extract all phone numbers |
| `extract.ips(text)` | Extract all IPv4 addresses |
| `extract.uuids(text)` | Extract all UUIDs |

### `is_match(pattern_name, value)`

| Parameter | Description |
|-----------|-------------|
| `pattern_name` | Pattern name string (e.g. `"email"`, `"ip_v4"`, `"uuid"`) |
| `value` | The string to validate |
| **Returns** | `bool` — True if the entire value matches |

## Development

```bash
pip install -e .
python -m pytest tests/ -v
```

## License

MIT
