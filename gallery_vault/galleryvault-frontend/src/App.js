// src/App.js

import React from 'react';
import Login from './components/Login';
import Register from './components/Register';
import UploadPhoto from './components/UploadPhoto';
import Gallery from './components/Gallery';

function App() {
  return (
    <div>
      <h1>Gallery Vault</h1>
      <Register />
      <Login />
      <UploadPhoto />
      <Gallery />
    </div>
  );
}

export default App;
