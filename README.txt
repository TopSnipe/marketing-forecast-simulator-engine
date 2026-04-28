# Marketing Campaign Engine  
Version: v0.2.0  
Environment: Development  

The Marketing Campaign Engine is a modular, src‑layout Python application that simulates a single business workflow: triggering a marketing campaign and calculating how much inventory should be restocked based on projected demand. Users enter a merchandise ID and expected demand increase, and the system generates a restock recommendation including quantity and total cost.

This project demonstrates:

- Multi‑module program design  
- JSON file handling  
- Classes and domain modeling  
- Separation of concerns (domain, persistence, services, CLI)  
- Error handling and input validation  
- Configuration‑driven architecture  
- Clean src‑layout packaging  

---

## Project Structure (src‑layout)


### Module Responsibilities

| Module | Purpose |
|--------|---------|
| `engine.py`     | Domain model, repositories, services, CLI workflow |
| `config.py`     | Loads settings.cfg, resolves paths, environment setup |
| `main.py`       | Entry point for the CLI application |
| `settings.cfg`  | Centralized configuration for paths, defaults, logging |
| `data/`         | JSON input/output files |

---

## Core Features (v0.2.0)

- Trigger Marketing Campaign  
- Demand Projection Logic  
- Restock Recommendation Output  
- JSON Persistence  
- Input Validation & Error Handling  
- Configuration‑driven defaults  
- Clean CLI interface  

---

## Dependencies

This project uses only:

- Python Standard Library  
- `pytest` (optional, for testing)

No external runtime dependencies are required.

---

## How to Run

### 1. Navigate to the project root
