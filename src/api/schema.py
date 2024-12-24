from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    category: str
    date: str

class BudgetCreate(BaseModel):
    category: str
    limit: float