from fastapi import FastAPI
from utilities.database import engine
from utilities.models import Base
from apis.order_views import order_router
from apis.user_views import user_router
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(user_router)
app.include_router(order_router)

# Run with python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
