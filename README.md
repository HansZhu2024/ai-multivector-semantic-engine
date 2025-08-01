# AI-Driven Multi-Vector Semantic Analysis Platform

**AI-driven semantic vector platform for natural language-based data understanding and automatic SQL generation.**

## Overview

This project introduces a multi-vector semantic analysis framework powered by AI. It encodes both **data content** and **program semantics** into vector representations across several semantic layers. By leveraging vector search and LLM-based reasoning, the system enables **natural language-driven exploration** of structured data, automatic SQL generation, and schema understanding — even for undocumented or complex databases.

## Key Features

- 🔍 **Multi-faceted semantic modeling**  
  Encodes field values, code usage, view logic, and procedure behavior into distinct vector spaces.

- 💬 **Natural language query interface**  
  Accepts user prompts and translates them into intelligent SQL queries through vector retrieval and LLM inference.

- 🔗 **Semantic alignment and reasoning**  
  Supports synonym detection, schema mapping, and semantic lineage across database objects.

- ⚙️ **Modular architecture**  
  Designed for extensibility with optional support for views, stored procedures, and multilingual data environments.

## System Architecture

The system organizes semantics across five vector databases:

| Vector DB | Description                                      |
|-----------|--------------------------------------------------|
| **A**     | Field Content Semantics – data value distribution, field meaning |
| **B**     | Code Usage Semantics – CRUD context from application code |
| **C**     | Semantic Integration Layer – high-level alignment across sources |
| **D**     | View Semantics (optional) – joins, aggregations, filters |
| **E**     | Stored Procedure Semantics (optional) – logic and parameter meaning |

### Example Pipeline

```python
# Step 1: Embed field value semantics
description = "This column contains order creation timestamps like 2024-01-01"
vector = model.encode(description)
vector_db_A.insert(vector)

# Step 2: Analyze source code context
code_snippet = "db.query(Order).filter(Order.created_at >= '2024-01-01')"
summary = local_llm(f"Describe semantic intent:\n{code_snippet}")
vector_db_B.insert(model.encode(summary))

# Step 3: Handle a natural language query
query = "Analyze the order volume from Q1 to Q4 in 2024"
query_vec = model.encode(query)

# Step 4: Retrieve related fields from semantic databases
results = {
    "A": vector_db_A.search(query_vec),
    "B": vector_db_B.search(query_vec),
    "D": vector_db_D.search(query_vec),
    "E": vector_db_E.search(query_vec),
}

# Step 5: Feed into prompt for SQL generation
prompt = assemble_prompt(query, results)
sql = local_llm(prompt)
```

Use Cases
🧠 AI SQL Copilot – Generate SQL from plain language questions

🔄 Cross-System Field Mapping – Discover related fields in large schemas

📊 Automated Reporting – Dynamically generate dashboards and analytics

🔍 Schema Understanding – Understand undocumented or legacy databases

🧾 Data Governance – Trace semantic lineage across fields and systems

For now, this is a research prototype. If you’re interested in collaboration or contributing, feel free to open an issue or contact the maintainer.

---

## License

MIT License

## Contact

For feedback, discussion, or collaboration:

**Hans Zhu**  
✉️ [hanszhu687@gmail.com]
