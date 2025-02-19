from flask import Blueprint, current_app, jsonify

from ..factory import get_statistics_repository

stats_blueprint = Blueprint("stats_blueprint", __name__)


@stats_blueprint.route("/api/v1/stats/<table_name>", methods=["GET"])
def table_count(table_name):
    stats_repo = get_statistics_repository(current_app.config)
    if stats_repo.check_table_name(table_name):
        row = stats_repo.get_number_of_rows(table_name)
        return jsonify({"message": "Number of Rows", "rows": row}), 200
    return jsonify({"message": "Table name not found"}), 404


# -------------------- New AI-Powered Endpoints --------------------


@stats_blueprint.route("/api/v1/generate-content/<int:customer_id>", methods=["GET"])
def generate_content(customer_id):
    """Mock LLM response to generate personalized content for a customer."""
    MOCK_LLM_RESPONSES = {
        1: "Dear Jedi,\n\nThank you for reaching out regarding our latest products...",
        2: "Hello Batman,\n\nWe appreciate your time and interest in our offerings...",
        3: "Dear Santa Claus,\n\nThank you for your continued trust in our products...",
        4: "Dear Mover,\n\nWe value your feedback on drug efficacy...",
    }

    content = MOCK_LLM_RESPONSES.get(
        customer_id, "Dear Customer,\n\nWe appreciate your engagement..."
    )

    return jsonify(
        {
            "customer_id": customer_id,
            "generated_content": {"Content_type": "email", "Content": content},
        }
    )


@stats_blueprint.route("/api/v1/summarized_interactions/<int:customer_id>", methods=["GET"])
def summarize_interactions(customer_id):
    """Mock LLM-based summarization of customer interactions."""
    summary_data = {
        "total_interactions": 5,
        "most_frequent_channel": "Email",
        "last_interaction": {"date": "2024-01-25", "channel": "Call", "topic": "Product inquiry"},
        "key_topics": ["Product inquiry", "Drug efficacy", "Regulatory compliance"],
        "summary_text": f"Customer {customer_id} frequently contacts us via email, inquiring about drug efficacy, dosage recommendations, and regulatory compliance.",
    }

    return jsonify({"customer_id": customer_id, "summary": summary_data})


@stats_blueprint.route("/api/v1/interaction-stats", methods=["GET"])
def interaction_stats():
    """Mocked statistics on interactions per product for each customer type."""
    stats = {"Red": {"Sand": 3}, "Orange": {"Sand": 2}, "Blue": {"Sand": 1}}

    return jsonify({"interaction_statistics": stats})
