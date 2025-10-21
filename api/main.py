from fastapi import FastAPI
app = FastAPI()

from company_routes import company_router
from login_routes import login_router
from questions_routes import pergunta_router
app.include_router(company_router)
app.include_router(login_router)
app.include_router(pergunta_router)