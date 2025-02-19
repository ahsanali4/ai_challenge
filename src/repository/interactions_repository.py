import psycopg2

from src.config import Config
from src.repository.base import interactionRepository
from src.utils.db.postgres import QueryRunner


class InteractionsRepository(interactionRepository):
    """Fetches past customer interactions from the database."""

    def __init__(self, config: Config):
        self.runner = QueryRunner(config)

    def get_recent_interactions(self, customer_id, limit=5):
        """Fetch recent interactions for a customer."""
        query = """
        SELECT interaction, topic, sentiment
        FROM interactions
        WHERE customer_id = {customer_id}
        ORDER BY date_start DESC
        LIMIT {limit};
        """
        rows = self.runner.execute_query(query.format(customer_id=customer_id, limit=limit))

        return [{"interaction": r[0], "topic": r[1], "sentiment": r[2]} for r in rows]
