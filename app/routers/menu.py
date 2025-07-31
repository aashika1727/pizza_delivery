# app/routers/menu.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/menu", tags=["Menu"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MenuItem)
def add_menu_item(item: schemas.MenuItemBase, db: Session = Depends(get_db)):
    return crud.add_menu_item(db, item)

@router.get("/", response_model=list[schemas.MenuItem])
def get_menu(db: Session = Depends(get_db)):
    return crud.get_menu(db)
