import json
from src.marketing_engine.config import MA_WINDOW, ES_ALPHA, WMA_WEIGHTS

# ---------------------------------------------------------
# Forecasting Service
# ---------------------------------------------------------

SALES_HISTORY_FILE = "data/sales_history.json"

class ManualForecastingService:
    """Provides simple forecasting models."""

    @staticmethod
    def moving_average(data: list[int], window: int = MA_WINDOW) -> float:                  # window is the number of months to average over
        if len(data) < window:
            raise ValueError("Not enough data points for moving average.")
        return sum(data[-window:]) / window

    @staticmethod
    def weighted_moving_average(data: list[int], weights: list[float] = WMA_WEIGHTS) -> float:
        window = len(weights)
        if len(data) < window:
            raise ValueError("Not enough data points for weighted moving average.")

        recent = data[-window:]
        weighted_sum = sum(v * w for v, w in zip(recent, weights))
        total_weight = sum(weights)

        return weighted_sum / total_weight

    @staticmethod
    def exponential_smoothing(data: list[int], alpha: float = ES_ALPHA) -> float:
        if not data:
            raise ValueError("No data provided for exponential smoothing.")
        forecast = data[0]
        for value in data[1:]:
            forecast = alpha * value + (1 - alpha) * forecast
        return forecast

    @staticmethod
    def run() -> None:
        """CLI flow for running forecasting models."""
        
        print("\n=== Manual Demand Forecasting ===")

        raw = input("Enter historical demand (3–12 months of historical sales values in 1000s): ").strip()
        if not raw:
            print("No data entered.\n")
            return

        try:
            data = [int(x.strip()) for x in raw.split(",")]
        except ValueError:
            print("Invalid input. Please enter integers only.\n")
            return

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

        print("------------------------\n")
        
    @staticmethod
    def load_sales_history(merch_id: str) -> list[int]:
        """Load monthly sales history for a merch item and return list of sales ints."""
        with open(SALES_HISTORY_FILE, "r") as file:
            data = json.load(file)

        if merch_id not in data:
            raise KeyError(f"No sales history found for merch ID {merch_id}")

        return [m["sales"] for m in data[merch_id]["monthly_sales"]]

    @staticmethod
    def forecast_next_quarter(merch_id: str, alpha: float = ES_ALPHA) -> dict:
        """
        Forecast the next 3 months (next quarter) using the last 3 years (36 months)
        of historical sales data and exponential smoothing.
        """
        history = ManualForecastingService.load_sales_history(merch_id)

        if len(history) < 36:
            raise ValueError("Not enough data for 3-year quarterly forecasting.")

        last_36 = history[-36:]  # last 3 years

        forecasts = []
        temp_series = last_36.copy()

        # Forecast 3 months ahead
        for _ in range(3):
            next_month = ManualForecastingService.exponential_smoothing(temp_series, alpha)
            forecasts.append(round(next_month, 2))
            temp_series.append(next_month)

        return {
            "merch_id": merch_id,
            "next_quarter_monthly": forecasts,
            "next_quarter_total": round(sum(forecasts), 2)
        }        
        