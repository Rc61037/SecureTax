'use client';
import { useTaxFormStore } from '@/store/useTaxFormStore';

export default function Step1Demographics() {
  const { name, updateField, nextStep } = useTaxFormStore();

  const handleNext = () => {
    if (name.trim() === '') {
      alert("Please enter your name");
      return;
    }
    nextStep();
  };

  return (
    <div className="step-container">
      <h2>Step 1: Personal Details</h2>
      <p>Please enter your Full Name. This is securely encrypted at rest.</p>
      
      <div className="input-group">
        <label htmlFor="name">Full Name</label>
        <input 
          type="text" 
          id="name"
          className="input-field" 
          placeholder="John Doe" 
          value={name}
          onChange={(e) => updateField('name', e.target.value)}
        />
      </div>

      <div className="btn-group" style={{ justifyContent: 'flex-end' }}>
        <button className="btn" onClick={handleNext}>Continue</button>
      </div>
    </div>
  );
}
