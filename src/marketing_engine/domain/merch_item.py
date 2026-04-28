# ---------------------------------------------------------
# Domain Model
# ---------------------------------------------------------

class MerchItem:
    """
    Domain model representing a merchandise item.
    """

    def __init__(self, merch_id: str, name: str, unit_cost: float, current_stock: int, base_demand: int):
        self.merch_id = merch_id
        self.name = name
        self.unit_cost = unit_cost
        self.current_stock = current_stock
        self.base_demand = base_demand

    def __repr__(self):
        return f"<MerchItem {self.merch_id}: {self.name}>"

