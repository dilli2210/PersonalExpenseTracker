from fastapi import APIRouter
from .schema import BudgetCreate
from .services.budgets import set_budget_service, get_budgets_service

router = APIRouter()

@router.get("/api/budgets")
def list_budgets():
    """List all budgets."""
    return get_budgets_service()

@router.post("/api/budgets")
def create_budget(budget: BudgetCreate):
    """Set or update a budget."""
    set_budget_service(budget.dict())
    return {"message": "Budget set successfully"}