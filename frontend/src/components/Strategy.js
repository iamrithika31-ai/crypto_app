import React, { useState } from "react";
import axios from "axios";

function Strategy() {
  const [data, setData] = useState([]);

  const run = () => {
    axios.post("http://127.0.0.1:8000/strategy/run")
      .then(res => setData(res.data));
  };

  return (
    <div>
      <h2>Strategy</h2>
      <button onClick={run}>Run</button>

      {data.map((d, i) => (
        <div key={i}>
          {d.symbol} → {d.signal}
        </div>
      ))}
    </div>
  );
}

export default Strategy;