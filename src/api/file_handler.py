import json
from typing import List,Dict
import os
from collections import OrderedDict

# Get the current working directory
current_path = os.getcwd()
default_data_file = os.path.join(current_path, "src\\api\\data", "expense.json")
DATA_FILE = default_data_file

def load_expense_data() -> Dict:
    """Load expenses and budgets from the JSON file."""
    try:
        print("current_path",current_path)
        print("default_data_file",default_data_file)
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"expenses": [], "budgets": []}


def save_expense_data(data: Dict):
    """Save expenses and budgets to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_expense(expense: Dict):
    """Add a new expense."""
    data = load_expense_data()
    if data["expenses"]:
        max_id = max(exp.get("id", 0) for exp in data["expenses"])  # Find the maximum current ID
        next_id = max_id + 1
    else:
        next_id = 1 # Start at 1 if no expenses exist

    # Add the ID to the expense
    ordered_expense = OrderedDict([
        ("id", next_id),
        ("description", expense["description"]),
        ("amount", expense["amount"]),
        ("category", expense["category"]),
        ("date", expense["date"]),
    ]) 

    data["expenses"].append(ordered_expense)
    save_expense_data(data)

def get_all_expenses() -> List[Dict]:
    """Retrieve all expenses."""
    data = load_expense_data()
    return data["expenses"]

def set_budget(budget: Dict):
    """Set or update a budget."""
    data = load_expense_data()
    for b in data["budgets"]:
        if b["category"] == budget["category"]:
            b["limit"] = budget["limit"]
            save_expense_data(data)
            return
    data["budgets"].append(budget)
    save_expense_data(data)

def get_budgets() -> List[Dict]:
    """Retrieve all budgets."""
    data = load_expense_data()
    return data["budgets"]    