from dataclasses import dataclass


@dataclass(frozen=True)
class AgentLimits:
    max_steps: int = 5
    max_tool_calls: int = 8


def validate_limits(limits: AgentLimits) -> None:
    if not 1 <= limits.max_steps <= 20:
        raise ValueError("max_steps must be between 1 and 20")
    if not 0 <= limits.max_tool_calls <= 50:
        raise ValueError("max_tool_calls must be between 0 and 50")
