from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./test.db"

Base = declarative_base()

class Patron(Base):
    __tablename__ = 'patrons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    body_mass = Column(Float)
    consumptions = relationship("Consumption", back_populates="patron")  # Adjusted for clarity

class Drink(Base):
    __tablename__ = 'drinks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    abv = Column(Float)  # Alcohol by volume as a percentage
    consumptions = relationship("Consumption", back_populates="drink")  # Adjusted for clarity

class Consumption(Base):
    __tablename__ = 'consumption'
    id = Column(Integer, primary_key=True, index=True)
    patron_id = Column(Integer, ForeignKey('patrons.id'))
    drink_id = Column(Integer, ForeignKey('drinks.id'))
    amount = Column(Float)  # Amount in milliliters
    timestamp = Column(DateTime, default=datetime.utcnow)

    patron = relationship("Patron", back_populates="consumptions")
    drink = relationship("Drink", back_populates="consumptions")

# Set up the database session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
