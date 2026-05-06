import Sidebar from './Sidebar';
import Header from './Header';
export default function AppLayout({ children }: { children: React.ReactNode }) {
  return <div className="layout"><Sidebar /><main className="content"><Header />{children}</main></div>;
}
