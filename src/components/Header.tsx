import { usePolicy } from '../utils/PolicyContext';
import StatusBadge from './StatusBadge';
export default function Header(){const {userEmail,status}=usePolicy(); return <header className='header'><div>Insurance Policy Lifecycle Portal</div><div><span>{userEmail}</span> <StatusBadge status={status}/></div></header>}
