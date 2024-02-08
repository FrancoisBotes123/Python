from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from datetime import datetime

# Assuming you've created models.py and schemas.py as discussed
from models import SessionLocal, engine, Patron as DBPatron, Drink as DBDrink, Consumption as DBConsumption
from schemas import Patron, PatronCreate, Drink, DrinkCreate, Consumption, ConsumptionCreate
from logic import calculate_saturation  # Correctly import the function

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/patrons/", response_model=Patron)
def create_patron(patron: PatronCreate, db: Session = Depends(get_db)):
    db_patron = DBPatron(**patron.dict())
    db.add(db_patron)
    db.commit()
    db.refresh(db_patron)
    return db_patron

@app.get("/patrons/", response_model=List[Patron])
def list_patrons(db: Session = Depends(get_db)):
    db_patrons = db.query(DBPatron).all()
    return db_patrons

@app.get("/patrons/{patron_id}", response_model=Patron)
def read_patron(patron_id: int, db: Session = Depends(get_db)):
    db_patron = db.query(DBPatron).filter(DBPatron.id == patron_id).first()
    if db_patron is None:
        raise HTTPException(status_code=404, detail="Patron not found")
    return db_patron

@app.post("/drinks/", response_model=Drink)
def create_drink(drink: DrinkCreate, db: Session = Depends(get_db)):
    db_drink = DBDrink(**drink.dict())
    try:
        db.add(db_drink)
        db.commit()
        db.refresh(db_drink)
    except IntegrityError:
        db.rollback()  # Roll back the transaction
        raise HTTPException(status_code=400, detail="Drink with this name already exists.")
    return db_drink

@app.post("/consumptions/", response_model=Consumption)
def record_consumption(consumption: ConsumptionCreate, db: Session = Depends(get_db)):
    consumption_data = consumption.dict()
    consumption_data["timestamp"] = datetime.utcnow()  # Ensure timestamp is set to current time
    db_consumption = DBConsumption(**consumption_data)
    db.add(db_consumption)
    db.commit()
    db.refresh(db_consumption)
    return db_consumption

@app.get("/patrons/{patron_id}/saturation/")
def get_saturation(patron_id: int, db: Session = Depends(get_db)):
    # Correctly use the calculate_saturation function with the db session
    saturation = calculate_saturation(patron_id, db)
    return {"patron_id": patron_id, "saturation": saturation}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
