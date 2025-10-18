from fastapi import FastAPI
app = FastAPI()

from company_routes import company_router
app.include_router(company_router)