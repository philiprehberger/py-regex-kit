import pytest
from philiprehberger_regex_kit import patterns, extract, is_match


def test_email_pattern_matches_valid():
    assert patterns.EMAIL.fullmatch("user@example.com") is not None
    assert patterns.EMAIL.fullmatch("first.last+tag@sub.domain.org") is not None
    assert patterns.EMAIL.fullmatch("not-an-email") is None
    assert patterns.EMAIL.fullmatch("missing@") is None


def test_url_extraction():
    text = "Visit https://example.com and http://test.org/page?q=1 for info."
    result = extract.urls(text)
    assert len(result) == 2
    assert "https://example.com" in result
    assert "http://test.org/page?q=1" in result


def test_ip_v4_pattern():
    assert patterns.IP_V4.fullmatch("192.168.1.1") is not None
    assert patterns.IP_V4.fullmatch("255.255.255.255") is not None
    assert patterns.IP_V4.fullmatch("0.0.0.0") is not None
    assert patterns.IP_V4.fullmatch("999.999.999.999") is None
    assert patterns.IP_V4.fullmatch("256.1.1.1") is None


def test_phone_extraction():
    text = "Call +1 (555) 123-4567 or 800-555-0199 for support."
    result = extract.phones(text)
    assert len(result) == 2


def test_is_match_function():
    assert is_match("email", "user@example.com") is True
    assert is_match("email", "not-valid") is False
    assert is_match("ip_v4", "10.0.0.1") is True
    assert is_match("uuid", "550e8400-e29b-41d4-a716-446655440000") is True
    assert is_match("hex_color", "#ff00aa") is True
    assert is_match("date_iso", "2026-03-21") is True


def test_is_match_unknown_pattern():
    with pytest.raises(ValueError, match="Unknown pattern"):
        is_match("nonexistent", "test")


def test_uuid_pattern():
    valid = "550e8400-e29b-41d4-a716-446655440000"
    assert patterns.UUID.fullmatch(valid) is not None
    assert patterns.UUID.fullmatch("not-a-uuid") is None
    assert patterns.UUID.fullmatch("550e8400-e29b-41d4-a716") is None


def test_email_extraction():
    text = "Contact alice@example.com and bob@test.org for details."
    result = extract.emails(text)
    assert "alice@example.com" in result
    assert "bob@test.org" in result


def test_uuid_extraction():
    text = "IDs: 550e8400-e29b-41d4-a716-446655440000 and 6ba7b810-9dad-11d1-80b4-00c04fd430c8"
    result = extract.uuids(text)
    assert len(result) == 2


def test_ip_extraction():
    text = "Servers at 192.168.1.1 and 10.0.0.1 are running."
    result = extract.ips(text)
    assert "192.168.1.1" in result
    assert "10.0.0.1" in result


def test_is_match_case_insensitive_name():
    assert is_match("EMAIL", "user@example.com") is True
    assert is_match("Ip_V4", "127.0.0.1") is True


def test_mac_address_pattern():
    assert patterns.MAC_ADDRESS.fullmatch("00:1A:2B:3C:4D:5E") is not None
    assert patterns.MAC_ADDRESS.fullmatch("00:1A:2B") is None


def test_domain_pattern():
    assert patterns.DOMAIN.fullmatch("example.com") is not None
    assert patterns.DOMAIN.fullmatch("sub.domain.org") is not None


def test_time_24h_pattern():
    assert patterns.TIME_24H.fullmatch("23:59") is not None
    assert patterns.TIME_24H.fullmatch("00:00:00") is not None
    assert patterns.TIME_24H.fullmatch("25:00") is None
