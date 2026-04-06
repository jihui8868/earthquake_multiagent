# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Earthquake multi-agent system built with Python 3.13. Uses deepagents, FastAPI, LangChain (OpenAI), and SQLAlchemy.

## Development Setup

This project uses **uv** for package management.

```bash
# Install dependencies
uv sync

# Run the app
uv run python app/main.py
```

## Architecture

- `app/main.py` — Application entry point
- `app/multi_agent.py/` — Multi-agent module (currently empty, to be built out)
- `pyproject.toml` — Project config and dependencies managed by uv

## Key Dependencies

- **deepagents** — Multi-agent orchestration framework
- **FastAPI** — HTTP API layer
- **langchain-openai** — LLM integration via LangChain's OpenAI bindings
- **SQLAlchemy** — Database ORM
