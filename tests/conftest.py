"""Test configuration for Enterprise Knowledge Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "enterprise-knowledge-agent", "category": "Executive"}
