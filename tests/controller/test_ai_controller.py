def test_stats_endpoint(client):
    """Test statistics endpoint"""
    response = client.get("/api/v1/stats/some_table")
    assert response.status_code in [200, 404]  # Table may or may not exist
    assert "message" in response.json


def test_generate_content_endpoint(client):
    """Test AI content generation endpoint with mock LLM"""
    response = client.get("/api/v1/generate-content/1")
    assert response.status_code == 200
    assert "generated_content" in response.json


def test_summarized_interactions_endpoint(client):
    """Test AI summarization endpoint with mock LLM and RAG"""
    response = client.get("/api/v1/summarized_interactions/1")
    assert response.status_code == 200
    assert "summary" in response.json


def test_interaction_stats(client):
    response = client.get("/api/v1/interaction-stats")
    assert response.status_code == 200
    assert "interaction_statistics" in response.json
