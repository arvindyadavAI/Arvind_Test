import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import { PolicyProvider } from './utils/PolicyContext';
import './styles/global.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <PolicyProvider>
        <App />
      </PolicyProvider>
    </BrowserRouter>
  </React.StrictMode>,
);
