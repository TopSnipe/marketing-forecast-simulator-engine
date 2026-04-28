# System Architecture

```text
marketing-simulation-engine/
│
├── data/
│   ├── merch_catalog.json
│   ├── sales_history.json
│   ├── restock_recommendations.json
│
├── src/
│   └── marketing_engine/
│       │
│       ├── cli/
│       │   └── main_menu.py              # CLI orchestration
│       │
│       ├── domain/
│       │   └── merch_items.py            # Domain models
│       │
│       ├── persistence/
│       │   ├── merch_repository.py       # Catalog persistence
│       │   ├── restock_repository.py     # Restock persistence
│       │
│       ├── routing/
│       │   └── process_router.py         # Workflow routing
│       │
│       ├── services/
│       │   ├── manual_forecasting_service.py
│       │   ├── historical_forecasting_service.py
│       │   ├── marketing_service.py
│       │
│       ├── utils/
│       │   ├── seed_merch_catalog.py     # Catalog generator (set at 100)
│       │   ├── seed_sales_history.py     # Sales generator (set at 36‑month)
│       │   └── __init__.py
│       │
│       ├── config.py                     # Forecasting configuration
│       └── __init__.py
│
├── docs/
├── main.py                               # Application entry point
├── README.md
├── pyproject.toml
├── settings.cfg
├── screenshots/
└── demo_video_link.txt

```
