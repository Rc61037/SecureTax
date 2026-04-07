'use client';
import { useTaxFormStore } from '@/store/useTaxFormStore';
import Step1Demographics from './Step1Demographics';
import Step2Income from './Step2Income';
import Step3Deductions from './Step3Deductions';
import Step4Review from './Step4Review';

export default function TaxForm() {
  const { step } = useTaxFormStore();
  
  const renderStep = () => {
    switch (step) {
      case 1: return <Step1Demographics />;
      case 2: return <Step2Income />;
      case 3: return <Step3Deductions />;
      case 4: return <Step4Review />;
      default: return <Step1Demographics />;
    }
  };

  const progressPercentage = ((step - 1) / 3) * 100;

  return (
    <div className="glass-container">
      <div className="progress-container">
        <div 
          className="progress-bar" 
          style={{ width: `${progressPercentage}%` }}
        ></div>
      </div>
      {renderStep()}
    </div>
  );
}
