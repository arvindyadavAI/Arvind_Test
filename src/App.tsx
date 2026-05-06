import { Navigate, Route, Routes } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import AccountPage from './pages/AccountPage';
import PolicyInfoPage from './pages/PolicyInfoPage';
import UnderwritingPage from './pages/UnderwritingPage';
import PolicyFormsPage from './pages/PolicyFormsPage';
import PricingPage from './pages/PricingPage';
import { usePolicy } from './utils/PolicyContext';

const Protected = ({ children }: { children: JSX.Element }) => {
  const { isAuthenticated } = usePolicy();
  return isAuthenticated ? children : <Navigate to="/login" replace />;
};

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/" element={<Navigate to="/account" replace />} />
      <Route path="/account" element={<Protected><AccountPage /></Protected>} />
      <Route path="/policy-info" element={<Protected><PolicyInfoPage /></Protected>} />
      <Route path="/underwriting" element={<Protected><UnderwritingPage /></Protected>} />
      <Route path="/policy-forms" element={<Protected><PolicyFormsPage /></Protected>} />
      <Route path="/pricing" element={<Protected><PricingPage /></Protected>} />
    </Routes>
  );
}
