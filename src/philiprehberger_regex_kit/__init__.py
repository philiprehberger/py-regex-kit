"""Pre-built, tested regex patterns for common data formats."""

from __future__ import annotations

import re


__all__ = [
    "patterns",
    "extract",
    "replace",
    "is_match",
]


class patterns:
    """Compiled regex patterns for common data formats."""

    EMAIL: re.Pattern[str] = re.compile(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    )

    URL: re.Pattern[str] = re.compile(
        r"https?://[^\s<>\"')\]]+",
    )

    IP_V4: re.Pattern[str] = re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"
    )

    IP_V6: re.Pattern[str] = re.compile(
        r"\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b"
    )

    PHONE: re.Pattern[str] = re.compile(
        r"\+?\d[\d\s\-().]{7,}\d"
    )

    UUID: re.Pattern[str] = re.compile(
        r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
        r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"
    )

    HEX_COLOR: re.Pattern[str] = re.compile(
        r"#(?:[0-9a-fA-F]{3}){1,2}\b"
    )

    DATE_ISO: re.Pattern[str] = re.compile(
        r"\b\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])\b"
    )

    TIME_24H: re.Pattern[str] = re.compile(
        r"\b(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?\b"
    )

    CREDIT_CARD: re.Pattern[str] = re.compile(
        r"\b(?:\d[ -]*?){13,19}\b"
    )

    MAC_ADDRESS: re.Pattern[str] = re.compile(
        r"\b[0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5}\b"
    )

    DOMAIN: re.Pattern[str] = re.compile(
        r"\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b"
    )


class extract:
    """Static methods for extracting pattern matches from text."""

    @staticmethod
    def emails(text: str) -> list[str]:
        """Extract all email addresses from text."""
        return patterns.EMAIL.findall(text)

    @staticmethod
    def urls(text: str) -> list[str]:
        """Extract all URLs from text."""
        return patterns.URL.findall(text)

    @staticmethod
    def phones(text: str) -> list[str]:
        """Extract all phone numbers from text."""
        return patterns.PHONE.findall(text)

    @staticmethod
    def ips(text: str) -> list[str]:
        """Extract all IPv4 addresses from text."""
        return patterns.IP_V4.findall(text)

    @staticmethod
    def uuids(text: str) -> list[str]:
        """Extract all UUIDs from text."""
        return patterns.UUID.findall(text)


class replace:
    """Static methods for replacing pattern matches in text."""

    @staticmethod
    def emails(text: str, replacement: str = "[EMAIL]") -> str:
        """Replace all email addresses in text."""
        return patterns.EMAIL.sub(replacement, text)

    @staticmethod
    def urls(text: str, replacement: str = "[URL]") -> str:
        """Replace all URLs in text."""
        return patterns.URL.sub(replacement, text)

    @staticmethod
    def phones(text: str, replacement: str = "[PHONE]") -> str:
        """Replace all phone numbers in text."""
        return patterns.PHONE.sub(replacement, text)

    @staticmethod
    def ips(text: str, replacement: str = "[IP]") -> str:
        """Replace all IPv4 addresses in text."""
        return patterns.IP_V4.sub(replacement, text)


_PATTERN_MAP: dict[str, re.Pattern[str]] = {
    "email": patterns.EMAIL,
    "url": patterns.URL,
    "ip_v4": patterns.IP_V4,
    "ip_v6": patterns.IP_V6,
    "phone": patterns.PHONE,
    "uuid": patterns.UUID,
    "hex_color": patterns.HEX_COLOR,
    "date_iso": patterns.DATE_ISO,
    "time_24h": patterns.TIME_24H,
    "credit_card": patterns.CREDIT_CARD,
    "mac_address": patterns.MAC_ADDRESS,
    "domain": patterns.DOMAIN,
}


def is_match(pattern_name: str, value: str) -> bool:
    """Check if a value fully matches a named pattern.

    Args:
        pattern_name: One of 'email', 'url', 'ip_v4', 'ip_v6', 'phone',
            'uuid', 'hex_color', 'date_iso', 'time_24h', 'credit_card',
            'mac_address', 'domain'.
        value: The string to test.

    Returns:
        True if the entire value matches the pattern.

    Raises:
        ValueError: If the pattern name is not recognized.
    """
    pattern = _PATTERN_MAP.get(pattern_name.lower())
    if pattern is None:
        msg = (
            f"Unknown pattern: '{pattern_name}'. "
            f"Available: {', '.join(sorted(_PATTERN_MAP))}"
        )
        raise ValueError(msg)
    return pattern.fullmatch(value) is not None
