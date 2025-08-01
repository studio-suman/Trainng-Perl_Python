import React, { useState } from 'react';
import axios from 'axios';

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false); // Spinner state

  const sendMessage = async () => {
    if (!input.trim()) return;
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/api/chat', { message: input });
      setMessages([...messages, { user: input }, { bot: res.data.response }]);
      setInput('');
    } catch (error) {
      console.error('Error sending message:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100 px-4">
      <h2 className="text-2xl font-bold mb-4">Chatbot</h2>
      <div className='border p-4 mb-4 items-center justify-center h-200 w-full max-w-md bg-white rounded shadow'>
        <div className="border p-4 mb-4 h-64 w-full max-w-md overflow-y-scroll bg-white rounded shadow">
          {messages.map((msg, i) => (
            <div key={i} className="mb-2">
              <strong>{msg.user ? 'You' : 'Bot'}:</strong> {msg.user || msg.bot}
            </div>
          ))}
          {loading && (
            <div className="flex justify-center mt-4">
              <div className="w-6 h-6 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
            </div>
          )}
        </div> 
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="border p-2 w-full max-w-md mb-2 rounded"
          placeholder="Type your message..."
          disabled={loading}
        />
        <button
          onClick={sendMessage}
          className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600 w-full max-w-md disabled:opacity-50"
          disabled={loading}
        >
          {loading ? 'Sending...' : 'Send'}
        </button>
      </div>
    </div>
  );
}

export default Chatbot;
