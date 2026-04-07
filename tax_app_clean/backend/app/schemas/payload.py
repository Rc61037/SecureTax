from pydantic import BaseModel, Field

class TaxFormData(BaseModel):
    name: str = Field(..., min_length=2, description="User's full name")
    w2_income: float = Field(..., ge=0, description="Cannot be negative")
    itemized_deductions: float = Field(0.0, ge=0)

class CalculationResponse(BaseModel):
    status: str
    tax_owed: float
    effective_rate_percent: float
