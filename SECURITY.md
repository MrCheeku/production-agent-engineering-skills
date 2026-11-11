# Security Policy

## Supported versions

Security fixes are prioritized for the latest version on the default branch. Older releases may not receive fixes unless explicitly stated.

## Reporting a vulnerability

Do not publish exploitable details in a public issue. Use GitHub private vulnerability reporting for this repository when available. Otherwise contact the maintainer privately through the contact method on the GitHub profile.

Include affected paths/versions, impact, minimal reproduction, and safe mitigation. Do not include credentials or other people's personal data.

## Security principles

- Store secrets in environment variables or a secret manager.
- Use unmistakably fake example credentials.
- Apply least privilege to API tokens, CI permissions, and device access.
- Validate untrusted inputs and authorize each side effect server-side.
- Use timeouts and bounded retries.
- Never execute model-generated shell commands or arbitrary code by default.
- Treat public username lookup as limited public information retrieval, not identity verification.
- Do not bypass login controls, CAPTCHAs, rate limits, or website restrictions.
- Keep sensitive values out of logs, tests, screenshots, and issue reports.

Examples are educational, not a security certification. Review auth, authorization, network exposure, dependencies, retention, and operations before production use.
