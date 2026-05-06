import { NavLink } from 'react-router-dom';
const links = [{t:'Account',p:'/account'},{t:'Policy Info',p:'/policy-info'},{t:'Underwriting',p:'/underwriting'},{t:'Policy Forms',p:'/policy-forms'},{t:'Pricing',p:'/pricing'}];
export default function Sidebar(){return <aside className='sidebar'><h2>TopInsurance</h2>{links.map(l=><NavLink key={l.p} to={l.p} className='nav'>{l.t}</NavLink>)}</aside>}
