from fastapi import FastAPI
from app.database import Base, engine

# Import routes
from app.routes import transaction, summary, user

# Create FastAPI app
app = FastAPI(title="Finance Tracker API")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(transaction.router, prefix="/transactions", tags=["Transactions"])
app.include_router(summary.router, prefix="/summary", tags=["Summary"])
app.include_router(user.router, prefix="/users", tags=["Users"])


@app.get("/")
def home():
    return {"message": "Finance API is running 🚀"}