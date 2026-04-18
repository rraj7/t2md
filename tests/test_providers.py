import pytest

from t2md.providers import PROVIDERS, AnthropicProvider, OpenAIProvider, get_provider


def test_openai_routes_small_input_to_mini():
    assert OpenAIProvider().select_model(100) == "gpt-4o-mini"


def test_openai_routes_medium_input_to_full_model():
    assert OpenAIProvider().select_model(10_000) == "gpt-4o"


def test_openai_routes_large_input_to_large_model():
    assert OpenAIProvider().select_model(100_000) == "gpt-4o"


def test_anthropic_routes_small_input_to_haiku():
    assert AnthropicProvider().select_model(100) == "claude-haiku-4-5"


def test_anthropic_routes_medium_input_to_sonnet():
    assert AnthropicProvider().select_model(10_000) == "claude-sonnet-4-6"


def test_get_provider_is_case_insensitive():
    assert get_provider("OpenAI").name == "openai"
    assert get_provider("  anthropic  ").name == "anthropic"


def test_get_provider_rejects_unknown():
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("gemini")


def test_providers_registry_contains_both():
    assert set(PROVIDERS) == {"openai", "anthropic"}


def test_complete_raises_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        OpenAIProvider().complete("test", "gpt-4o-mini", 1000)


def _make_openai_fake(finish_reason="stop"):
    class FakeMsg:
        content = "  mocked response  "

    class FakeChoice:
        message = FakeMsg()

    FakeChoice.finish_reason = finish_reason

    class FakeResp:
        choices = [FakeChoice()]

    class FakeClient:
        def __init__(self, api_key):
            assert api_key == "sk-test"
            self.chat = self
            self.completions = self

        def create(self, model, messages, max_tokens):
            assert model == "gpt-4o-mini"
            assert messages[0]["content"] == "hi"
            assert max_tokens == 1234
            return FakeResp()

    return FakeClient


def test_complete_calls_openai_sdk(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    import openai
    monkeypatch.setattr(openai, "OpenAI", _make_openai_fake(finish_reason="stop"))

    text, truncated = OpenAIProvider().complete("hi", "gpt-4o-mini", 1234)
    assert text == "mocked response"
    assert truncated is False


def test_complete_flags_truncation_when_length_finish(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    import openai
    monkeypatch.setattr(openai, "OpenAI", _make_openai_fake(finish_reason="length"))

    _, truncated = OpenAIProvider().complete("hi", "gpt-4o-mini", 1234)
    assert truncated is True
