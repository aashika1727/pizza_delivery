# app/schemas.py
from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional
from datetime import datetime
import re

class CustomerBase(BaseModel):
    name: str
    phone: str
    email: EmailStr
    address: str

    @validator('phone')
    def validate_phone(cls, value):
        pattern = re.compile(r'^[6-9]\d{9}$')
        if not pattern.match(value):
            raise ValueError('Invalid phone number. Must be a 10-digit Indian number starting with 6-9.')
        return value

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    class Config:
        orm_mode = True

class MenuItemBase(BaseModel):
    name: str
    size: str
    price: float
    availability: str

class MenuItem(MenuItemBase):
    id: int
    class Config:
        orm_mode = True

class OrderItemCreate(BaseModel):
    pizza_id: int
    quantity: int

class OrderCreate(BaseModel):
    customer_id: int
    items: List[OrderItemCreate]

class Order(BaseModel):
    id: int
    customer_id: int
    order_time: datetime
    status: str
    class Config:
        orm_mode = True
