import { useNavigate } from 'react-router-dom';
import AppLayout from '../components/AppLayout';
import SummaryCard from '../components/SummaryCard';
export default function AccountPage(){const nav=useNavigate();return <AppLayout><h2>Account Dashboard</h2><div className='grid4'><SummaryCard title='Total Policies' value={16}/><SummaryCard title='Draft Policies' value={4}/><SummaryCard title='Quoted Policies' value={7}/><SummaryCard title='Issued Policies' value={5}/></div><button className='primary' onClick={()=>nav('/policy-info')}>Start New Policy</button></AppLayout>}
