from flask import Blueprint, jsonify

from src.services.ai_service import AIService

# Flask Blueprint
ai_blueprint = Blueprint("ai", __name__)
ai_service = AIService()


@ai_blueprint.route("/api/v1/generate-content/<int:customer_id>", methods=["GET"])
def generate_content_api(customer_id):
    """Flask API handler for generating AI-powered content."""
    content = ai_service.generate_content(customer_id)
    return jsonify({"customer_id": customer_id, "generated_content": content})


@ai_blueprint.route("/api/v1/summarized_interactions/<int:customer_id>", methods=["GET"])
def summarize_interactions_api(customer_id):
    """Flask API handler for summarizing customer interactions."""
    summary = ai_service.summarize_interactions(customer_id)
    return jsonify({"customer_id": customer_id, "summary": summary})
