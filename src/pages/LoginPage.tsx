import { FormEvent, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { DEMO_CREDENTIALS } from '../data/mockData';
import { usePolicy } from '../utils/PolicyContext';

export default function LoginPage(){const nav=useNavigate();const {update}=usePolicy();const [email,setEmail]=useState('');const [password,setPassword]=useState('');const [error,setError]=useState('');
const submit=(e:FormEvent)=>{e.preventDefault(); if(!email||!password) return setError('Email and password are required.'); if(email===DEMO_CREDENTIALS.email&&password===DEMO_CREDENTIALS.password){update({isAuthenticated:true,userEmail:email});nav('/account')} else setError('Invalid demo credentials.');};
return <div className='login-wrap'><div className='login-card'><h1>TopInsurance</h1><p>Secure platform for policy lifecycle management.</p><form onSubmit={submit}><input placeholder='Email address' value={email} onChange={e=>setEmail(e.target.value)}/><input type='password' placeholder='Password' value={password} onChange={e=>setPassword(e.target.value)}/>{error&&<p className='error'>{error}</p>}<button>Sign In</button></form><small>Demo: demo@topinsurance.com / Password123</small></div></div>}
