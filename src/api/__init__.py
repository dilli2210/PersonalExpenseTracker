from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(docs_url="/")

    from . import expenses
    from . import budgets
    app.include_router(expenses.router)
    app.include_router(budgets.router)

    return app