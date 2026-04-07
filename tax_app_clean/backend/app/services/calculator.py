from decimal import Decimal

class FederalTaxCalculator:
    # 2025 Expected Single Filer Brackets
    BRACKETS_2025_SINGLE = [
        {"rate": Decimal("0.10"), "up_to": Decimal("11925")},
        {"rate": Decimal("0.12"), "up_to": Decimal("48475")},
        {"rate": Decimal("0.22"), "up_to": Decimal("103350")},
        {"rate": Decimal("0.24"), "up_to": Decimal("197300")},
        {"rate": Decimal("0.32"), "up_to": Decimal("250525")},
        {"rate": Decimal("0.35"), "up_to": Decimal("626350")},
        {"rate": Decimal("0.37"), "up_to": Decimal("Infinity")},
    ]

    STANDARD_DEDUCTION_2025_SINGLE = Decimal("15000")

    @classmethod
    def calculate_single(cls, gross_income: Decimal, itemized_deductions: Decimal = Decimal("0")) -> dict:
        total_deduction = max(cls.STANDARD_DEDUCTION_2025_SINGLE, itemized_deductions)
        taxable_income = max(Decimal("0"), gross_income - total_deduction)
        
        tax_owed = Decimal("0")
        previous_bracket_limit = Decimal("0")
        
        for bracket in cls.BRACKETS_2025_SINGLE:
            if taxable_income > previous_bracket_limit:
                current_limit = bracket["up_to"] if bracket["up_to"] != Decimal("Infinity") else taxable_income
                taxable_in_bracket = min(
                    taxable_income - previous_bracket_limit, 
                    current_limit - previous_bracket_limit
                )
                tax_owed += taxable_in_bracket * bracket["rate"]
                previous_bracket_limit = current_limit
            else:
                break
                
        effective_rate = (tax_owed / gross_income * 100) if gross_income > 0 else Decimal("0")
        
        return {
            "gross_income": float(gross_income),
            "total_deduction": float(total_deduction),
            "taxable_income": float(taxable_income),
            "tax_owed": round(float(tax_owed), 2),
            "effective_rate": round(float(effective_rate), 2)
        }
