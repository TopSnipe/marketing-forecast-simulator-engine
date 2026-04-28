from src.marketing_engine.service.marketing_service import MarketingService
from src.marketing_engine.config import DEFAULT_DEMAND_INCREASE
from src.marketing_engine.persistence.merch_repository import MerchRepository
from src.marketing_engine.persistence.restock_repository import RestockRepository

# ---------------------------------------------------------
# Process Function
# ---------------------------------------------------------

def trigger_marketing_campaign() -> None:
    """CLI flow: prompt user, run marketing logic, save and display results."""
    
    print("\n=== Trigger Marketing Campaign ===")

    merch_id = input("Enter merch ID: ").strip()
    if not merch_id:
        print("Merch ID is required.\n")
        return

    demand_input = input(f"Expected demand increase (default {DEFAULT_DEMAND_INCREASE}): ").strip()  # DEFAULT_DEMAND_INCREASE is a percentage (set at .20 for 20% in settings.cfg)

    if demand_input == "":
        demand_increase = DEFAULT_DEMAND_INCREASE
    else:
        try:
            demand_increase = float(demand_input)
        except ValueError:
            print("Invalid demand increase. Using default.")
            demand_increase = DEFAULT_DEMAND_INCREASE

    # Load merch item as a domain object
    try:
        merch_item = MerchRepository.get_merch_item(merch_id)
    except FileNotFoundError:
        print("Merch catalog file not found.\n")
        return
    except ValueError as exc:
        print(f"Invalid merch catalog: {exc}\n")
        return
    except KeyError:
        print("Merch item not found.\n")
        return

    # Run business logic
    result = MarketingService.calculate_restock(merch_item, demand_increase)

    # Save result
    RestockRepository.save_recommendation(result)

    # Display output
    print("\n--- Restock Recommendation ---")
    print(f"Item: {result['name']} ({result['merch_id']})")
    print(f"Recommended Quantity: {result['restock_qty']}")
    print(f"Total Cost: ${result['total_cost']}")
    print("------------------------------\n\n")