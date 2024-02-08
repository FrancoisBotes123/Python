from sqlalchemy.orm import Session
from models import Patron, Drink, Consumption
from datetime import datetime, timedelta

def calculate_saturation(patron_id: int, db: Session):
    # Fetch the patron and their consumptions directly, using the provided session
    patron = db.query(Patron).filter(Patron.id == patron_id).first()
    if not patron:
        return 0
    
    total_saturation = 0
    current_time = datetime.utcnow()
    
    consumptions = db.query(Consumption).filter(Consumption.patron_id == patron_id).all()
    for consumption in consumptions:
        # Calculate the time decay
        time_diff = current_time - consumption.timestamp
        # Assuming alcohol metabolism rate of 0.015 per hour
        decay_factor = max(0, 1 - (time_diff.total_seconds() / 3600) * 0.015)
        
        # Assuming the amount is in milliliters and converting to liters for the calculation
        # and assuming pure alcohol density approx 0.789 g/ml
        alcohol_grams = consumption.amount * (consumption.drink.abv / 100) * 0.789
        # Calculate the saturation for this consumption, considering body mass
        saturation = alcohol_grams / (patron.body_mass * 1000) * decay_factor
        total_saturation += saturation
    
    return total_saturation
