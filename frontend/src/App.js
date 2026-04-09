import React, { useState } from "react";

function App() {
  const [user, setUser] = useState({
    user_id: "",
    name: "",
    phone: "",
    consent: true
  });

  const [cart, setCart] = useState({
    user_id: "",
    items: ""
  });

  const [response, setResponse] = useState("");

  const API = "http://127.0.0.1:8000";

  const registerUser = async () => {
    const res = await fetch(`${API}/user/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(user)
    });
    const data = await res.json();
    setResponse(JSON.stringify(data, null, 2));
  };

  const addCart = async () => {
    const res = await fetch(`${API}/cart/cart`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_id: cart.user_id,
        items: cart.items.split(",")
      })
    });
    const data = await res.json();
    setResponse(JSON.stringify(data, null, 2));
  };

  const sendMessage = async () => {
    const res = await fetch(`${API}/message/send/${cart.user_id}`);
    const data = await res.json();
    setResponse(JSON.stringify(data, null, 2));
  };

  const getAnalytics = async () => {
    const res = await fetch(`${API}/analytics/`);
    const data = await res.json();
    setResponse(JSON.stringify(data, null, 2));
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>🚀 SmartEngage AI Dashboard</h1>

      <h2>👤 Register User</h2>
      <input placeholder="User ID" onChange={e => setUser({...user, user_id: e.target.value})}/>
      <input placeholder="Name" onChange={e => setUser({...user, name: e.target.value})}/>
      <input placeholder="Phone" onChange={e => setUser({...user, phone: e.target.value})}/>
      <button onClick={registerUser}>Register</button>

      <h2>🛒 Add Cart</h2>
      <input placeholder="User ID" onChange={e => setCart({...cart, user_id: e.target.value})}/>
      <input placeholder="Items (comma separated)" onChange={e => setCart({...cart, items: e.target.value})}/>
      <button onClick={addCart}>Add to Cart</button>

      <h2>📩 Generate Message</h2>
      <button onClick={sendMessage}>Send Message</button>

      <h2>📊 Analytics</h2>
      <button onClick={getAnalytics}>View Analytics</button>

      <h3>Response:</h3>
      <pre>{response}</pre>
    </div>
  );
}

export default App;