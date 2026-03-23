import React, { useEffect, useState } from "react";
import axios from "axios";

function Analytics() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/analytics")
      .then(res => setData(res.data));
  }, []);

  return (
    <div>
      <h2>Analytics</h2>
      {data.map((d, i) => (
        <div key={i}>
          {d.symbol} | {d.price_change_pct}% | Vol: {d.volume_change_pct}%
        </div>
      ))}
    </div>
  );
}

export default Analytics;