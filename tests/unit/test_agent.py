"""Enterprise Knowledge Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_search_knowledge():
    """Test Search enterprise knowledge base with natural language."""
    tools = AgentTools()
    result = await tools.search_knowledge(query="test", sources="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_answer_question():
    """Test Answer a question using internal knowledge sources."""
    tools = AgentTools()
    result = await tools.answer_question(question="test", context="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_index_document():
    """Test Index a document into the enterprise knowledge base."""
    tools = AgentTools()
    result = await tools.index_document(document_path="test", metadata="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_identify_knowledge_gaps():
    """Test Identify topics with insufficient or outdated documentation."""
    tools = AgentTools()
    result = await tools.identify_knowledge_gaps(domain="test", min_freshness_days=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.enterprise_knowledge_agent_agent import EnterpriseKnowledgeAgentAgent
    agent = EnterpriseKnowledgeAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
