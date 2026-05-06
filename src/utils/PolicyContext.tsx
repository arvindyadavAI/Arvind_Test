import { createContext, useContext, useMemo, useState } from 'react';
import { PolicyState } from './types';

const initialState: PolicyState = {
  isAuthenticated: false,
  userEmail: '',
  status: 'Draft',
  policyNumber: '',
  policyInfo: {
    applicantName: '', businessName: '', email: '', phone: '', address: '', policyType: 'General Liability',
    effectiveDate: '', expirationDate: '', coverageLimit: 100000, deductible: 1000,
  },
  underwriting: { priorClaims: 'No', cancellations: 'No', employees: 5, revenue: 250000, locationType: 'Office', safetyProgram: 'Yes' },
  selectedForms: [],
};

const Ctx = createContext<any>(null);
export const PolicyProvider = ({ children }: { children: React.ReactNode }) => {
  const [state, setState] = useState<PolicyState>(() => {
    const saved = localStorage.getItem('topinsurance-state');
    return saved ? JSON.parse(saved) : initialState;
  });
  const update = (patch: Partial<PolicyState>) => setState((s: PolicyState) => {
    const n = { ...s, ...patch };
    localStorage.setItem('topinsurance-state', JSON.stringify(n));
    return n;
  });
  const value = useMemo(() => ({ ...state, update }), [state]);
  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
};
export const usePolicy = () => useContext(Ctx);
