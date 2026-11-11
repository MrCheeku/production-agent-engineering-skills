---
name: mcp-server-development
description: "Build and test Model Context Protocol servers with scoped tools, resources, prompts, and secure execution."
version: "1.0.0"
---

# Mcp Server Development

## Purpose

Expose application capabilities through MCP without coupling protocol concerns to domain logic or giving an agent unrestricted access.

## Activation

### Activate when

Building MCP servers, tools/resources/prompts, agent-host integrations, or MCP contract tests.

### Do not activate when

An internal function call is sufficient and no interoperable MCP client is needed.

## Required tools and inputs

SDK major version, transport, host expectations, capability list, authentication model, resource sensitivity, and execution permissions.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Keep domain functions independent from MCP. The server layer maps typed MCP inputs to application services and stable results. Use stdio for local subprocess integrations and Streamable HTTP for deployed network services. Verify the selected SDK version.

## Implementation workflow

1. Read current official SDK docs and pin the intended major. 2. Define minimum capabilities. 3. Give tools narrow names, typed schemas, and precise descriptions. 4. Validate inputs in the domain layer. 5. Add auth/authorization for remote deployments. 6. Keep stdio protocol output free of diagnostics. 7. Test handlers with an in-memory client when supported. 8. Test transport, cancellation, and failures.

## Coding standards

One tool performs one bounded operation. Return concise structured results. Document side effects and required confirmation. Avoid generic execute or shell tools.

## Security requirements

Authenticate network clients. Authorize every action independently of model instructions. Allowlist files, entities, services, and hosts. Require user confirmation for consequential actions. Treat arguments and resource contents as untrusted.

## Error handling and observability

Return useful errors without stack traces or secrets. Distinguish validation, authorization, dependency, and timeout failures. Apply deadlines and cancellation.

## Testing requirements

Test schema validation, valid calls, invalid calls, denied permissions, timeouts, and serialization. Prefer an in-memory client where supported and add transport smoke tests.

## Practical example

~~~python
from mcp.server import MCPServer

server = MCPServer("Demo")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

if __name__ == "__main__":
    server.run()
~~~

## Common mistakes and remedies

Do not mix stdout logging with stdio transport. Do not expose broad filesystem or shell tools. Do not assume a host enforces your permissions. Do not reuse older SDK samples without checking migration notes.

## Expected outputs

Version-pinned server, scoped capabilities, permission rules, tests, host configuration notes, and transport instructions.

## Production-readiness checklist

- Requirements and constraints are recorded.
- Boundaries and ownership are explicit.
- Inputs and outputs have documented contracts.
- Failure and recovery behavior is defined.
- Security controls are enforced outside untrusted model output.
- Tests cover normal, boundary, denied, and failing cases.
- Logs and metrics are useful and contain no secrets.
- Operational and compatibility limitations are documented.

## Quality-assurance checklist

SDK major version is explicit. Schemas are typed. Side effects are disclosed. Authorization is server-side. Denied/failing cases are tested.
