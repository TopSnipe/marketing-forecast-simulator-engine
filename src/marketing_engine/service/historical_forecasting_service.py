import json
from src.marketing_engine.config import MA_WINDOW, ES_ALPHA, WMA_WEIGHTS
from src.marketing_engine.service.manual_forecasting_service import ManualForecastingService

# ---------------------------------------------------------
# Forecasting Service
# ---------------------------------------------------------

SALES_HISTORY_FILE = "data/sales_history.json"

class HistoricalForecastingService:
    """Runs forecasting using the last 36 months of generated sales history."""

    @staticmethod
    def run() -> None:
        print("\n=== Historical Sales Forecasting ===")

        # Load JSON
        try:
            with open(SALES_HISTORY_FILE, "r") as file:
                history = json.load(file)
        except FileNotFoundError:
            print("No sales history found. Please seed historical sales data first.\n")
            return

        # Pick the first merch item for forecasting
        merch_id = next(iter(history.keys()))
        monthly_sales = [m["sales"] for m in history[merch_id]["monthly_sales"]]

        # Use last 36 months
        data = monthly_sales[-36:]

        print(f"\nUsing last 36 months of sales for merch ID: {merch_id}")
        print(f"Data points: {len(data)} months")

        print("\n--- Forecast Results ---")

        # Moving Average
        try:
            ma = ManualForecastingService.moving_average(data, MA_WINDOW)
            print(f"Moving Average (window={MA_WINDOW}): {ma:.2f}")
        except ValueError as exc:
            print(f"MA Error: {exc}")

        # Weighted Moving Average
        try:
            wma = ManualForecastingService.weighted_moving_average(data, WMA_WEIGHTS)
            print(f"Weighted Moving Average (weights={WMA_WEIGHTS}): {wma:.2f}")
        except ValueError as exc:
            print(f"WMA Error: {exc}")

        # Exponential Smoothing
        try:
            es = ManualForecastingService.exponential_smoothing(data, ES_ALPHA)
            print(f"Exponential Smoothing (alpha={ES_ALPHA}): {es:.2f}")
        except ValueError as exc:
            print(f"ES Error: {exc}")


