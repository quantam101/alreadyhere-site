"""Regression tests for the secret-marker scanner.

Guards against false positives (env-var references, substrings such as
"disk-write") while still catching committed secret values.
"""

from runtime.security_scanner import scan_text


def test_env_var_reference_is_not_flagged():
    assert scan_text("GEMINI_API_KEY=${GEMINI_API_KEY}") == []
    assert scan_text("API_KEY=$GEMINI_API_KEY") == []
    assert scan_text("API_KEY=") == []


def test_sk_substring_inside_word_is_not_flagged():
    assert scan_text('"""Async disk-write engine consuming packets."""') == []


def test_literal_api_key_value_is_flagged():
    assert scan_text("API_KEY=AIzaSyREAL_LOOKING_VALUE") != []


def test_sk_key_prefix_is_flagged():
    assert scan_text("token = 'sk-ant-api03-abcdef'") != []


def test_named_secret_markers_still_match():
    assert scan_text("ANTHROPIC_API_KEY") != []
    assert scan_text("-----BEGIN PRIVATE KEY-----") != []
