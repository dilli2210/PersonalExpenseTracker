from pydantic import BaseModel

class Expense(BaseModel):
    id: int
    description: str
    amount: float
    category: str
    date: str

class Budget(BaseModel):
    category: str
    limit: float    