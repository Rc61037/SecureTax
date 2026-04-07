from fastapi import APIRouter
from decimal import Decimal
from app.schemas.payload import TaxFormData, CalculationResponse
from app.services.calculator import FederalTaxCalculator
from app.core.crypto import encrypt_data

router = APIRouter()

@router.post("/submit", response_model=CalculationResponse)
def submit_and_calculate_tax(data: TaxFormData):
    """
    1. Validates input automatically via Pydantic.
    2. Encrypts sensitive PII before any DB interaction.
    3. Runs tax bracket algorithms.
    """
    sensitive_payload = {
        "name": data.name,
        "w2_income": data.w2_income,
        "itemized_deductions": data.itemized_deductions
    }
    encrypted_data = encrypt_data(sensitive_payload)
    
    # In a full run:
    # db_record = EncryptedTaxData(encrypted_payload=encrypted_data, session_id=...)
    # db.add(db_record); db.commit()

    result = FederalTaxCalculator.calculate_single(
        gross_income=Decimal(str(data.w2_income)),
        itemized_deductions=Decimal(str(data.itemized_deductions))
    )
    
    return CalculationResponse(
        status="success",
        tax_owed=result["tax_owed"],
        effective_rate_percent=result["effective_rate"]
    )
