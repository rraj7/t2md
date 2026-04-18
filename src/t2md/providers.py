from __future__ import annotations

import os
from abc import ABC, abstractmethod
from typing import ClassVar

import tiktoken


def count_tokens(prompt: str) -> int:
    """Rough token count. Uses OpenAI's tokenizer for all providers — accurate
    for GPT models and close enough for routing decisions on other providers."""
    enc = tiktoken.encoding_for_model("gpt-4o")
    return len(enc.encode(prompt))


class Provider(ABC):
    name: ClassVar[str]
    env_key: ClassVar[str | None]
    tiers: ClassVar[list[tuple[int, str]]]
    large_model: ClassVar[str]

    def select_model(self, tokens: int) -> str:
        for threshold, model in self.tiers:
            if tokens < threshold:
                return model
        return self.large_model

    @abstractmethod
    def complete(self, prompt: str, model: str) -> str: ...

    def require_key(self) -> str:
        if self.env_key is None:
            return ""
        key = os.getenv(self.env_key)
        if not key:
            raise RuntimeError(
                f"{self.env_key} is not set. Export it in your shell: export {self.env_key}=..."
            )
        return key


class OpenAIProvider(Provider):
    name = "openai"
    env_key = "OPENAI_API_KEY"
    tiers = [(4_000, "gpt-4o-mini"), (32_000, "gpt-4o")]
    large_model = "gpt-4o"

    def complete(self, prompt: str, model: str) -> str:
        from openai import OpenAI

        client = OpenAI(api_key=self.require_key())
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.choices[0].message.content.strip()


class AnthropicProvider(Provider):
    name = "anthropic"
    env_key = "ANTHROPIC_API_KEY"
    tiers = [(4_000, "claude-haiku-4-5"), (32_000, "claude-sonnet-4-6")]
    large_model = "claude-sonnet-4-6"

    def complete(self, prompt: str, model: str) -> str:
        import anthropic

        client = anthropic.Anthropic(api_key=self.require_key())
        resp = client.messages.create(
            model=model,
            max_tokens=8096,
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.content[0].text.strip()


class OllamaProvider(Provider):
    """Local Ollama server. Not yet wired into CLI — placeholder for v0.3."""

    name = "ollama"
    env_key = None
    tiers = [(4_000, "llama3.2:3b"), (32_000, "llama3.1:8b")]
    large_model = "llama3.1:70b"

    def complete(self, prompt: str, model: str) -> str:
        raise NotImplementedError("Ollama support is planned for v0.3")


PROVIDERS: dict[str, type[Provider]] = {
    "openai": OpenAIProvider,
    "anthropic": AnthropicProvider,
}


def get_provider(name: str) -> Provider:
    key = name.lower().strip()
    if key not in PROVIDERS:
        available = ", ".join(PROVIDERS.keys())
        raise ValueError(f"Unknown provider '{name}'. Available: {available}")
    return PROVIDERS[key]()
