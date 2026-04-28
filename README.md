# Marketing Forcast Simulation Engine  
Version: v0.3.0  
Environment: Development  

The Marketing Simulation Engine is a modular, src‑layout Python application that models a complete business workflow: generating random historical sales data, forecasting future demand using (MA, WMA, ES), and triggering marketing campaigns that produce inventory restock recommendations. The system supports both automated forecasting (using 3‑year synthetic sales history) and manual forecasting (user‑provided demand values for learning and testing).

AI Assistance Statement:  
This project was completed with limited use of AI. Throughout development, I used Microsoft Copilot as a learning resource outside of my coding environment, primarily for questions related to information systems architecture, debugging strategies, and conceptual explanations. I also conducted extensive personal research into src‑layout project structures, virtual environment setup, version control practices, and general professional coding standards. The conversational guidance from Copilot helped me better understand errors, refine my approach, and standardize my project structure. All design decisions and written code were created and verified by me. Within Visual Studio Code, I received standard inline editor suggestions for syntax or structure; these were reviewed, modified, or rejected based on my own judgment to ensure the final implementation met the assignment requirements and reflected my personal coding style.

This project demonstrates:

- Clean src‑layout packaging (`src/marketing_engine/`)
- Multi‑module program design with clear separation of concerns  
- Domain modeling for merchandise and sales history  
- JSON‑based persistence for catalog and sales data  
- Forecasting models (MA, WMA, ES) in both manual and historical modes  
- Configuration‑driven architecture for weights, windows, and smoothing factors  
- Robust CLI orchestration with validation and error handling  
- Realistic business simulation of marketing‑driven restock decisions  
---

## Project Structure (src‑layout)

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

---

## Core Features (v0.3.0)

- Trigger Marketing Campaign  
- Historical Sales Forecasting (automated 36‑month dataset)  
- Manual Sales Forecasting (3–12 user‑provided values)  
- Demand Projection Logic  
- Restock Recommendation Output  
- JSON Persistence (catalog + sales history)  
- Synthetic Data Generation  
- CLI Menu System (src/marketing_engine/cli)  
- Routing Layer (src/marketing_engine/routing)  
- Utility Layer (src/marketing_engine/utils)  
- Configuration‑driven defaults  
- Error Handling & Input Validation   
---

## Dependencies

This project uses only:

- Python Standard Library  
- `pytest` (optional, for testing)

No external runtime dependencies are required.

---

## How to Run

### 1. Navigate to the project root
cd marketing-simulation-engine

### 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate     # macOS/Linux
.venv\Scripts\activate        # Windows

### 3. Run the application
python -m marketing_engine.main
