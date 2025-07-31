# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .routers import customers, menu, orders
from .database import Base, engine, SessionLocal
from . import crud, schemas

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(customers.router)
app.include_router(menu.router)
app.include_router(orders.router)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Direct route to create customer (for testing or fallback)
@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db=db, customer=customer)

