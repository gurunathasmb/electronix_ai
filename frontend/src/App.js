import { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    const res = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ text })
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Sentiment Analysis</h2>
      <textarea rows="4" cols="60" onChange={e => setText(e.target.value)} />
      <br />
      <button onClick={handlePredict}>Predict</button>
      {result && (
        <p>
          Sentiment: <strong>{result.label}</strong><br />
          Confidence: {result.score}
        </p>
      )}
    </div>
  );
}

export default App;
