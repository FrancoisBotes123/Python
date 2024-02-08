from pydantic import BaseModel
from typing import List
from datetime import datetime

class PatronBase(BaseModel):
    name: str
    body_mass: float

class PatronCreate(PatronBase):
    pass

class Patron(PatronBase):
    id: int
    class Config:
        orm_mode = True  # Keep orm_mode for compatibility unless you're sure you're using Pydantic V2 and want to switch to from_attributes

class DrinkBase(BaseModel):
    name: str
    abv: float

class DrinkCreate(DrinkBase):
    pass

class Drink(DrinkBase):
    id: int
    class Config:
        orm_mode = True  # Same note as above

class ConsumptionBase(BaseModel):
    patron_id: int
    drink_id: int
    amount: float
    timestamp: datetime  # Now correctly defined with the import at the top

class ConsumptionCreate(ConsumptionBase):
    pass

class Consumption(ConsumptionBase):
    id: int
    class Config:
        orm_mode = True  # And again, same note regarding orm_mode
