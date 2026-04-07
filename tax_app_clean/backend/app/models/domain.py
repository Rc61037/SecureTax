from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime)
    
class TaxSession(Base):
    __tablename__ = "tax_sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tax_year = Column(Integer, nullable=False)
    is_completed = Column(Boolean, default=False)

class EncryptedTaxData(Base):
    __tablename__ = "encrypted_tax_data"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("tax_sessions.id"), nullable=False)
    encrypted_payload = Column(String, nullable=False) 
    
class TaxResult(Base):
    __tablename__ = "tax_results"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("tax_sessions.id"), unique=True)
    total_income = Column(Float, nullable=False)
    standard_deduction = Column(Float, nullable=False)
    taxable_income = Column(Float, nullable=False)
    estimated_tax = Column(Float, nullable=False)
    effective_rate = Column(Float)
