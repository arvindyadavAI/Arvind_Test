import { PolicyInfo, RiskScore } from './types';

export const calculateRisk = (data: any): RiskScore => {
  let score = 0;
  if (data.priorClaims === 'Yes') score += 2;
  if (data.cancellations === 'Yes') score += 2;
  if (Number(data.employees) > 50) score += 1;
  if (Number(data.revenue) > 1000000) score += 1;
  if (data.locationType === 'High Hazard') score += 2;
  if (data.safetyProgram === 'No') score += 1;
  if (score <= 2) return 'Low Risk';
  if (score <= 5) return 'Medium Risk';
  return 'High Risk';
};

export const calculatePremium = (policy: PolicyInfo, risk: RiskScore, forms: string[]) => {
  const baseMap: Record<string, number> = {
    'General Liability': 1200,
    Property: 1500,
    Cyber: 1800,
    'Workers Compensation': 2100,
  };
  const basePremium = baseMap[policy.policyType] || 1000;
  const coverageFactor = policy.coverageLimit / 100000;
  const deductibleFactor = policy.deductible >= 5000 ? 0.9 : policy.deductible >= 2500 ? 0.97 : 1.1;
  const riskFactor = risk === 'Low Risk' ? 1 : risk === 'Medium Risk' ? 1.2 : 1.5;
  const formsCharge = forms.length * 75;
  const subtotal = basePremium * coverageFactor * deductibleFactor * riskFactor;
  const taxesFees = subtotal * 0.08;
  const totalPremium = subtotal + formsCharge + taxesFees;
  return { basePremium, riskAdjustment: subtotal - basePremium, formsCharge, taxesFees, totalPremium };
};
