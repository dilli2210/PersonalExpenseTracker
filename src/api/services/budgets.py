from ..file_handler import set_budget, get_budgets

def set_budget_service(budget: dict):
    set_budget(budget)

def get_budgets_service():
    return get_budgets()