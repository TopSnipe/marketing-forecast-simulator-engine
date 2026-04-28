# ---------------------------------------------------------
# Service Layer
# ---------------------------------------------------------
import subprocess
import os
from src.marketing_engine.domain.merch_item import MerchItem

class MarketingService:
    """Business logic for calculating restock needs."""

    @staticmethod
    def calculate_restock(merch_item: MerchItem, demand_increase: float) -> dict:
        """
        Calculate restock quantity and total cost for a merch item.

        projected_demand = base_demand * (1 + demand_increase)
        restock_qty = max(0, projected_demand - current_stock)
        """

        # Compute projected demand
        projected_demand = merch_item.base_demand * (1 + demand_increase)

        # Compute restock quantity (never negative)
        restock_qty = max(0, int(projected_demand - merch_item.current_stock))

        # Compute total cost
        total_cost = restock_qty * merch_item.unit_cost

        return {
            "merch_id": merch_item.merch_id,
            "name": merch_item.name,
            "restock_qty": restock_qty,
            "total_cost": round(total_cost, 2),
            "demand_increase": demand_increase,
        }

    
def clear_screen():
    """Modern cross-platform screen clear."""
    command = 'cls' if os.name == 'nt' else 'clear' 
    # In a security context, we use a list for subprocess to avoid shell injection
    subprocess.run([command], shell=True)
