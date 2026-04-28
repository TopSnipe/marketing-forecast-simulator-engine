import json
from src.marketing_engine.config import RESTOCK_OUTPUT

# ---------------------------------------------------------
# Persistence Layer
# ---------------------------------------------------------

class RestockRepository:
    """
    Handles saving restock recommendations to JSON.
    """

    @staticmethod
    def load_recommendations() -> list:
        """
        Load existing restock recommendations.
        Returns an empty list if file does not exist or is empty.
        """
        try:
            with open(RESTOCK_OUTPUT, "r") as file:
                content = file.read().strip()
            if not content:
                return []  # Empty file → treat as empty list
            return json.loads(content)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in restock recommendations file.")

    @staticmethod
    def save_recommendation(record: dict) -> None:
        """
        Append a new restock recommendation to the JSON file.
        """
        data = RestockRepository.load_recommendations()
        data.append(record)

        with open(RESTOCK_OUTPUT, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def save_and_return(record: dict) -> dict:
        """
        Convenience method:
        Saves the record and returns it for CLI display.
        """
        RestockRepository.save_recommendation(record)
        return record