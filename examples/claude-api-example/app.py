import os

from anthropic import Anthropic


def build_messages(prompt: str) -> list[dict[str, str]]:
    cleaned = prompt.strip()
    if not cleaned:
        raise ValueError("Prompt must not be empty")
    if len(cleaned) > 20_000:
        raise ValueError("Prompt is too long")
    return [{"role": "user", "content": cleaned}]


def ask(prompt: str) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    model = os.environ.get("ANTHROPIC_MODEL")
    if not api_key or not model:
        raise RuntimeError("Set ANTHROPIC_API_KEY and ANTHROPIC_MODEL")
    client = Anthropic(api_key=api_key, timeout=30.0, max_retries=2)
    response = client.messages.create(
        model=model,
        max_tokens=500,
        messages=build_messages(prompt),
    )
    text_blocks = [block.text for block in response.content if block.type == "text"]
    if not text_blocks:
        raise RuntimeError("The model returned no text block")
    return "\n".join(text_blocks)


if __name__ == "__main__":
    question = input("Prompt: ")
    print(ask(question))
