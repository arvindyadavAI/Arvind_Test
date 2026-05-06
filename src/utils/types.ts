export type PolicyStatus = 'Draft' | 'Quoted' | 'Booked' | 'Issued';
export type RiskScore = 'Low Risk' | 'Medium Risk' | 'High Risk';

export interface PolicyInfo {
  applicantName: string;
  businessName: string;
  email: string;
  phone: string;
  address: string;
  policyType: string;
  effectiveDate: string;
  expirationDate: string;
  coverageLimit: number;
  deductible: number;
}

export interface UnderwritingAnswers {
  priorClaims: string;
  cancellations: string;
  employees: number;
  revenue: number;
  locationType: string;
  safetyProgram: string;
}

export interface PolicyState {
  isAuthenticated: boolean;
  userEmail: string;
  status: PolicyStatus;
  policyNumber: string;
  policyInfo: PolicyInfo;
  underwriting: UnderwritingAnswers;
  selectedForms: string[];
}
