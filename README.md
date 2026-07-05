# Enterprise Knowledge Agent

[![CI](https://github.com/kogunlowo123/enterprise-knowledge-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/enterprise-knowledge-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Executive | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Enterprise knowledge management agent that indexes organizational knowledge, answers questions from internal sources, maintains institutional memory, identifies knowledge gaps, and facilitates knowledge sharing.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `search_knowledge` | Search enterprise knowledge base with natural language |
| `answer_question` | Answer a question using internal knowledge sources |
| `index_document` | Index a document into the enterprise knowledge base |
| `identify_knowledge_gaps` | Identify topics with insufficient or outdated documentation |
| `generate_knowledge_report` | Generate knowledge utilization and coverage report |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/enterprise-knowledge/synthesize` | Synthesize data |
| `POST` | `/api/v1/enterprise-knowledge/analyze` | Analyze |
| `GET` | `/api/v1/enterprise-knowledge/track` | Track metrics |
| `POST` | `/api/v1/enterprise-knowledge/recommend` | Get recommendation |
| `POST` | `/api/v1/enterprise-knowledge/report` | Generate report |

## Features

- Enterprise
- Knowledge
- Strategic Insights
- Decision Support

## Integrations

- Snowflake
- Tableau
- Salesforce
- Workday
- Jira

## Architecture

```
enterprise-knowledge-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── enterprise_knowledge_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Enterprise Data Platform + LLM + BI**

---

Built as part of the Enterprise AI Agent Platform.
