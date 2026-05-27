# GMAOS Enterprise Merge-Ready Pack

GMAOS is a zero-spend-first Global Multi-Agent Operating System built around EAOS, the Execution Automation Operating System runtime.

This package is designed as a merge-ready scaffold for a production-shaped, OCI Always Free, declarative, local-first agent control plane.

## Core Principle

Do not build a chatbot. Build a governed execution fabric.

```txt
Declarative VHLL Manifest
  -> No-Spend Policy Gate
  -> Context Minifier
  -> Vector Cache Interceptor
  -> Complexity Scorer
  -> Local Agent Swarm
  -> Verifier Loop
  -> Approval Gate
  -> Execution Adapter
  -> Audit Log
  -> Memory Commit
  -> Lifelong Catch and Correct
```

## Truthful Capability Standard

This scaffold is not literal ASI and is not certified military-grade. It is built for:

- ASI-aligned architecture: recursive improvement, verifier loops, memory compounding, multi-agent arbitration.
- Military-style hardening: zero-trust boundaries, least privilege, approval gates, audit logs, secret isolation, rollback.
- Production-ready path: tested, monitored, backed up, HTTPS-enabled, mobile-accessible, deployable.
- Live-ready merge standard: no paid adapters active, no placeholder production paths, no raw secrets.

## Zero-Spend Rule

Paid APIs, paid SaaS tasks, paid compute, paid storage, outbound sending, production deploys, and account mutations are blocked by default.

## First Merge Scope

- Declarative agent registry
- Declarative module registry
- Connector registry
- No-spend policy
- Approval policy
- Sovereign core runtime
- Cost guard
- Approval gate
- Audit log
- Local vector cache
- Complexity scorer
- Local research/document/content/engineering agent stubs
- Command center pages
- Docker Compose production-shaped stack
- OCI bootstrap script
- Security docs
- Launch checklist

## Local Runtime Smoke Test

```bash
cd gmaos
python3 -m runtime.sovereign_core
```

## Deployment Path

1. Provision OCI Always Free A1 instance.
2. Clone repo.
3. Run `deploy/oci-bootstrap.sh`.
4. Copy `.env.example` to `.env`.
5. Run `docker compose up -d --build`.
6. Run health checks.
7. Open command center.

## Non-Negotiables

- No raw secrets in frontend or repo.
- No paid adapters enabled by default.
- No execution without audit log.
- No risky external action without approval.
- No production claim until the production gate passes.


## Production Domain: alreadyherellc.com

This package is preconfigured for the GoDaddy domain `alreadyherellc.com`.

Recommended public routes:

```txt
alreadyherellc.com          Public site
app.alreadyherellc.com      Command center
api.alreadyherellc.com      EAOS runtime API
status.alreadyherellc.com   Uptime/status page
n8n.alreadyherellc.com      Automation server, protected only
```

The deployment uses `caddy/Caddyfile` for HTTPS reverse proxy routing. Configure DNS at GoDaddy or Cloudflare Free after the OCI public IP is known.

See `docs/DOMAIN_ALREADYHERELLC.md`.
