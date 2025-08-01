import React, { useState } from 'react';
import Login from './components/Login/Login';
import Chatbot from './components/Chatbot/Chatbot';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <div>
      {loggedIn ? <Chatbot /> : <Login onLogin={() => setLoggedIn(true)} />}
    </div>
  );
}

export default App;