import { create } from 'zustand';

export interface TaxFormState {
  step: number;
  name: string;
  w2Income: number | '';
  itemizedDeductions: number | '';
  setStep: (step: number) => void;
  nextStep: () => void;
  prevStep: () => void;
  updateField: (field: keyof TaxFormState, value: any) => void;
  reset: () => void;
}

export const useTaxFormStore = create<TaxFormState>((set) => ({
  step: 1,
  name: '',
  w2Income: '',
  itemizedDeductions: '',
  setStep: (step: number) => set({ step }),
  nextStep: () => set((state) => ({ step: state.step + 1 })),
  prevStep: () => set((state) => ({ step: state.step - 1 })),
  updateField: (field: keyof TaxFormState, value: any) => set({ [field]: value }),
  reset: () => set({ step: 1, name: '', w2Income: '', itemizedDeductions: '' })
}));
