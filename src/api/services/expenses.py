from ..file_handler import add_expense, get_all_expenses

def add_expense_service(expense:dict):
    add_expense(expense)

def get_expense_service():
    return get_all_expenses()