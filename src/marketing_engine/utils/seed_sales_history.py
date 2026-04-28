import json
import random
from datetime import datetime, timedelta
from src.marketing_engine.config import DATA_DIR, MERCH_CATALOG


OUTPUT_FILE = f"{DATA_DIR}/sales_history.json"


# Category-based baseline multipliers
CATEGORY_MULTIPLIERS = {  # Hypothetical multipliers that reflect typical demand patterns for each category as a revenue driver
    "Coffee": 1.4,        # steady, high-volume
    "Apparel": 1.0,       # moderate, seasonal 
    "Hats": 0.8,          # lower but steady   
    "Mugs": 0.6,          # small but consistent
    "Stickers": 0.5,      # low-volume impulse buys
    "Vet-Partner": 0.9    # moderate, mission-driven
}


def generate_monthly_dates(years=3):
    """Generate a list of month-start dates for the last N years."""
    today = datetime.today().replace(day=1)
    dates = []

    for i in range(years * 12):
        month = today - timedelta(days=30 * i)
        dates.append(month.strftime("%Y-%m"))

    return list(reversed(dates))


def seed_sales_history() -> None:
    """Generate 3 years of monthly sales history for all merch items."""
    
    with open(MERCH_CATALOG, "r") as file:                                  # Load merchandise catalog to get item details and base demand
        catalog = json.load(file)

    months = generate_monthly_dates(3)                                          # generate_monthly_dates loop function to create dates for the last 3 years
    history = {}                                                                # Initialize sales history in an empty dictionary

    # Loop to generate sales history for each item in the catalog, applying category-based multipliers and seasonal adjustments
    for merch_id, item in catalog.items():                                  
        category = item.get("category", "General")                             # Get category and base demand, with defaults if not specified
        base_demand = item.get("base_demand", 50)      # Base demand is a starting point for sales, which will be adjusted by multipliers and seasonal factors

        # Get the category multiplier, defaulting to 1.0 for any uncategorized items, which will scale the base demand according to typical sales patterns for that category
        multiplier = CATEGORY_MULTIPLIERS.get(category, 1.0)   # Demand curve mulitplier (base=1.0, increase=demand > base, decrease=demand < base)
        monthly_sales = []                                      # Initialize list to hold monthly sales data for the current item

        for month in months:
            # Add realistic variation
            seasonal = random.uniform(0.8, 1.2)   # Seasonal variance in Summer or Winter data (set to +-20% variance)
            noise = random.uniform(0.7, 1.3)        # Variance control limits of sales data (set to +-30% variance) 

            # Coffee gets a winter bump
            if category == "Coffee" and month.endswith(("-11", "-12", "-01")):       # November, December, January
                seasonal *= 1.25                                                     # Percent increase in sales during winter months for coffee

            # Apparel gets a summer dip
            if category == "Apparel" and month.endswith(("-06", "-07", "-08")):     # June, July, August
                seasonal *= 0.85                                                    # Percent decrease in sales during summer months for apparel

            sales = int(base_demand * multiplier * seasonal * noise)                # Calculate final sales data    
            monthly_sales.append({"month": month, "sales": sales})                  # Append to montthly_sales list as a dictionary with "month" and "sales" keys

        history[merch_id] = {                                                       # Store dict history     
            "name": item["name"],
            "category": category,
            "monthly_sales": monthly_sales
        }

    with open(OUTPUT_FILE, "w") as file:                                    # Open and save the generated sales history to a JSON file
        json.dump(history, file, indent=4)

    # Summary message indicating how many items were processed and where the output file is located
    print(f"Generated 3-year sales history for {len(catalog)} items → {OUTPUT_FILE}")  