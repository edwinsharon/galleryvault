// src/index.js

import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';  // You can create a global CSS file here if needed
import App from './App';  // Main App component
import { BrowserRouter as Router } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>
);
