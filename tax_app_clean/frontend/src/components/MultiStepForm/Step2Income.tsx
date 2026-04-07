'use client';
import { useTaxFormStore } from '@/store/useTaxFormStore';

export default function Step2Income() {
  const { w2Income, updateField, nextStep, prevStep } = useTaxFormStore();

  const handleNext = () => {
    if (w2Income === '' || w2Income < 0) {
      alert("Please enter a valid W2 Income.");
      return;
    }
    nextStep();
  };

  return (
    <div className="step-container">
      <h2>Step 2: W-2 Income</h2>
      <p>Enter your total wages, tips, and other compensation from your employer.</p>
      
      <div className="input-group">
        <label htmlFor="w2Income">Total W-2 Income ($)</label>
        <input 
          type="number" 
          id="w2Income"
          className="input-field" 
          placeholder="0.00" 
          value={w2Income}
          onChange={(e) => updateField('w2Income', parseFloat(e.target.value) || '')}
        />
      </div>

      <div className="btn-group">
        <button className="btn btn-secondary" onClick={prevStep}>Back</button>
        <button className="btn" onClick={handleNext}>Continue</button>
      </div>
    </div>
  );
}
