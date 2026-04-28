# ---------------------------------------------------------
# Persistence Layer
# ---------------------------------------------------------

import json
from src.marketing_engine.domain.merch_item import MerchItem
from src.marketing_engine.config import MERCH_CATALOG


class MerchRepository:
    """
    Handles loading merchandise data from the merch_catalog.json file.
    """

    @staticmethod
    def load_catalog() -> dict:
        """Load the entire merchandise catalog as a dictionary."""
        try:
            with open(MERCH_CATALOG, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Merch catalog file not found.")
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON in merch catalog: {exc}")

    @staticmethod
    def get_merch_item(merch_id: str) -> MerchItem:
        """
        Retrieve a single merchandise item by ID.
        Returns a MerchItem domain object.
        """
        catalog = MerchRepository.load_catalog()

        if merch_id not in catalog:
            raise KeyError(f"Merch ID '{merch_id}' not found in catalog.")

        data = catalog[merch_id]

        return MerchItem(
            merch_id=merch_id,
            name=data["name"],
            unit_cost=float(data["unit_cost"]),
            current_stock=int(data["current_stock"]),
            base_demand=int(data["base_demand"])
        )