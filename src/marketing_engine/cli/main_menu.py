from src.marketing_engine.utils.seed_sales_history import seed_sales_history
from src.marketing_engine.utils.seed_merch_catalog import seed_merch_catalog
from src.marketing_engine.routing.process_router import trigger_marketing_campaign
from src.marketing_engine.service.manual_forecasting_service import ManualForecastingService
from src.marketing_engine.service.historical_forecasting_service import HistoricalForecastingService
from src.marketing_engine.service.marketing_service import clear_screen


# ---------------------------------------------------------
# CLI Menu
# ---------------------------------------------------------

def main_menu() -> None:
    """Main CLI loop for the Marketing Engine."""
    clear_screen()
    
    while True:
        
        print("\n=== Marketing Engine ===")
        print("1. Trigger Marketing Campaign")
        print("2. Historical Sales Forecasting")
        print("3. Manual Sales Forecasting")
        print("4. Seed Merchandise Catalog")
        print("5. Seed Historical Sales Data")
        print("6. Exit")

        try:
            choice = input("Select an option: \n").strip()
        except KeyboardInterrupt:
            continue

        if choice == "1":
            try:
                trigger_marketing_campaign()
            except Exception as exc:
                print(f"Error occurred: {exc}")
                input("Press Enter to continue...")

        elif choice == "2":
            try:
                HistoricalForecastingService.run()
            except Exception as exc:
                print(f"Error occurred: {exc}")
                input("Press Enter to continue...")

        elif choice == "3":
            try:
                ManualForecastingService.run()
            except Exception as exc:
                print(f"Error occurred: {exc}")
                input("Press Enter to continue...")

        elif choice == "4":
            try:
                seed_merch_catalog()
            except Exception as exc:
                print(f"Error occurred: {exc}")
                input("Press Enter to continue...")
                
        elif choice == "5":
            try:
                seed_sales_history()
            except Exception as exc:
                print(f"Error occurred: {exc}")
                input("Press Enter to continue...")
                
        elif choice == "6":
            print("Exiting program...")
            clear_screen()
            break

        else:
            print("Invalid choice.\n")
            input("Press Enter to continue...")
            clear_screen()

