import TaxForm from '@/components/MultiStepForm/TaxForm';

export const metadata = {
  title: 'Secure Tax Prep',
  description: 'A highly secure, state-of-the-art tax preparation application.',
};

export default function Home() {
  return (
    <main>
      <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, marginBottom: '0.5rem', background: 'linear-gradient(to right, var(--accent), #c084fc)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
          SecureTax 2025
        </h1>
        <p style={{ maxWidth: '400px', margin: '0 auto' }}>
          Experience the fast, beautiful, and completely secure way to prepare your taxes.
        </p>
      </div>
      <TaxForm />
    </main>
  );
}
