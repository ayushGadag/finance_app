# 💰 Finance Tracker API

A backend system built using FastAPI to manage financial transactions with support for CRUD operations, filtering, summary analytics, and role-based access.

---

## 🚀 Features

- Create, Read, Update, Delete transactions
- Filter transactions by type and category
- Financial summary (income, expense, balance)
- Role-based access control (admin, viewer)
- Input validation using Pydantic

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

## 🧪 Test Cases

1. Create Transaction
- Input: valid data, role=admin
- Expected: success

2. Invalid Role
- Input: role=viewer
- Expected: 403 forbidden

3. Filtering
- Input: type=income
- Expected: only income records

4. Delete Transaction
- Input: valid ID
- Expected: record removed

5. Summary
- Input: multiple transactions
- Expected: correct balance

6. Invalid Input
- Input: negative amount
- Expected: validation error