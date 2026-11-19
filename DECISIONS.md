# ADR-001: Choosing FastAPI

## Status
Accepted

## Context

We are building FluxCore, a multi-tenant event-ingest and
webhook-delivery platform.

The system needs:

- Event ingestion
- API-key authentication
- Tenant isolation
- Idempotency
- PostgreSQL transactions
- Background delivery workers
- Redis-based rate limiting
- HMAC webhook signing
- Retry and dead-letter handling
- Observability
- Production deployment
- AI gateway with streaming support

## Decision

FastAPI is the selected backend framework
for the 24-week engineering project.

## Reasons

1. Native support for asynchronous endpoints.
2. Pydantic-based request and response validation.
3. Dependency injection through Depends.
4. Automatic OpenAPI documentation.
5. ASGI foundation through Starlette.
6. Explicit control over infrastructure and
   application architecture.

## Trade-offs

- No bundled ORM.
- No bundled migration system.
- No bundled authentication system.
- No built-in admin interface.
- Greater responsibility for assembling
  and maintaining infrastructure.
- Async programming requires careful
  management of blocking operations.

## Reopening Criteria

We will not change frameworks because of
hype, personal preference or isolated opinions.

Reopening requires:

1. Evidence from real job postings.
2. Measured performance limitations.
3. Operational issues attributable to the framework.
4. A clear engineering or business requirement.
5. A documented comparison with alternatives.

Week 17 includes a sanctioned Django comparison.
It is a measurement exercise, not permission
to change the selected stack.

## Consequences

FastAPI remains locked for all 24 weeks.

We will build and understand each architectural
layer instead of relying on framework magic.

## Review

End of Week 24.
