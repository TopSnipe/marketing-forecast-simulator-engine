import json
import random
from src.marketing_engine.config import MERCH_CATALOG


# ---------------------------------------------------------
# TSMG / HoleSnipe Product Definitions
# ---------------------------------------------------------

COFFEE_ROASTS = [
    "HoleSnipe Coffee - Midwatch Dark Roast",
    "HoleSnipe Coffee - TSMG Special Blend Medium Roast",
    "HoleSnipe Coffee - Reveille Light Roast",
    "HoleSnipe Coffee - Bootcamp Decaf Roast"
]

COFFEE_PRODUCTS = [
    f"HoleSnipe Coffee - {roast}" for roast in COFFEE_ROASTS
]

APPAREL_SIZES = ["S", "M", "L", "XL", "XXL"]

APPAREL_PRODUCTS = [
    "Get in the Hole! Hoodie",
    "Get in the Hole! T-Shirt",
    "HoleSnipe Logo Hoodie",
    "HoleSnipe Logo T-Shirt"
]

MUGS = [
    "HoleSnipe Coffee Mug",
    "TSMG Ceramic Mug",
    "Get in the Hole! Mug"
]

STICKERS = [
    "HoleSnipe Sticker Pack",
    "TSMG Logo Sticker",
    "Get in the Hole! Sticker"
]

HATS = [
    "HoleSnipe Trucker Hat",
    "TSMG Embroidered Hat",
    "Get in the Hole! Cap"
]

VET_PARTNER_PRODUCTS = [
    "RuckUp Leather Wallet (Vet-Owned)",
    "BravoZulu Paracord Bracelet (Vet-Owned)",
    "FireTeam Coffee Thermos (Vet-Owned)",
    "Recon Ridge Backpack (Vet-Owned)"
]


# ---------------------------------------------------------
# Seeder Function
# ---------------------------------------------------------

def seed_merch_catalog(count: int = 100) -> None:                       # default count of 100 merchandise items to seed into the catalog
    """
    Generate a realistic TSMG/HoleSnipe merchandise catalog.
    """
    catalog = {}

    # Build unified product list with categories
    product_pool = []

    # Coffee
    for name in COFFEE_PRODUCTS:
        product_pool.append(("Coffee", name))

    # Apparel (with sizes)
    for base_name in APPAREL_PRODUCTS:
        for size in APPAREL_SIZES:
            product_pool.append(("Apparel", f"{base_name} ({size})"))

    # Mugs
    for name in MUGS:
        product_pool.append(("Mugs", name))

    # Stickers
    for name in STICKERS:
        product_pool.append(("Stickers", name))

    # Hats
    for name in HATS:
        product_pool.append(("Hats", name))

    # Vet‑to‑Vet partner merch
    for name in VET_PARTNER_PRODUCTS:
        product_pool.append(("Vet‑Partner", name))

    # If count > product_pool, we cycle through
    for i in range(1, count + 1):
        merch_id = f"{i:03d}"
        category, name = random.choice(product_pool)

        # Pricing logic by category
        if category == "Coffee":
            unit_cost = round(random.uniform(10.0, 18.0), 2)            # variance range of cost (set 10-18 dollars) for coffee products
        elif category == "Apparel":
            unit_cost = round(random.uniform(20.0, 55.0), 2)            # variance range of cost (set 20-55 dollars) for apparel products
        elif category == "Mugs":
            unit_cost = round(random.uniform(8.0, 18.0), 2)             # variance range of cost (set 8-18 dollars) for mugs
        elif category == "Hats":
            unit_cost = round(random.uniform(15.0, 30.0), 2)             # variance range of cost (set 15-30 dollars) for hats    
        elif category == "Stickers":
            unit_cost = round(random.uniform(2.0, 8.0), 2)              # variance range of cost (set 2-8 dollars) for stickers
        else:  # Vet‑Partner
            unit_cost = round(random.uniform(12.0, 60.0), 2)            # variance range of cost (set 12-60 dollars) for vet-partner merch    

        catalog[merch_id] = {
            "name": name,
            "category": category,
            "unit_cost": unit_cost,
            "current_stock": random.randint(10, 250),
            "base_demand": random.randint(20, 300)
        }

    with open(MERCH_CATALOG, "w") as file:
        json.dump(catalog, file, indent=4)

    print()
    print(f"Seeded {count} TSMG/HoleSnipe merchandise items into {MERCH_CATALOG}")