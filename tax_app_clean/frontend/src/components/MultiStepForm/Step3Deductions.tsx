'use client';
import { useTaxFormStore } from '@/store/useTaxFormStore';

export default function Step3Deductions() {
  const { itemizedDeductions, updateField, nextStep, prevStep } = useTaxFormStore();

  const handleNext = () => {
    if (itemizedDeductions === '' || itemizedDeductions < 0) {
      alert("Please enter valid itemized deductions (enter 0 if none).");
      return;
    }
    nextStep();
  };

  return (
    <div className="step-container">
      <h2>Step 3: Deductions</h2>
      <p>Enter any itemized deductions. If you don't know, enter 0 and we will use the standard deduction.</p>
      
      <div className="input-group">
        <label htmlFor="deductions">Itemized Deductions ($)</label>
        <input 
          type="number" 
          id="deductions"
          className="input-field" 
          placeholder="0.00" 
          value={itemizedDeductions}
          onChange={(e) => updateField('itemizedDeductions', parseFloat(e.target.value) || 0)}
        />
      </div>

      <div className="btn-group">
        <button className="btn btn-secondary" onClick={prevStep}>Back</button>
        <button className="btn" onClick={handleNext}>Continue</button>
      </div>
    </div>
  );
}
