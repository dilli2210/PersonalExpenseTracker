from fastapi import APIRouter
from .schema import ExpenseCreate
from .services.expenses import add_expense_service,get_expense_service

router = APIRouter()

@router.get("/api/get-expenses")
def list_expenses():
    """List all expenses."""
    return get_expense_service()

@router.post("/api/expenses")
def create_expense(expense: ExpenseCreate):
    """Add a new expense."""
    add_expense_service(expense.dict())
    return {"message": "Expense added successfully"}