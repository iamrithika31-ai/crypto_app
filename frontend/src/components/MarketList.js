import React, { useEffect, useState } from "react";
import axios from "axios";

function MarketList() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/markets")
      .then(res => setData(res.data));
  }, []);

  return (
    <div>
      <h2>Market Data</h2>
      {data.map((d, i) => (
        <div key={i}>
          {d.symbol} | ${d.price} | Vol: {d.volume}
        </div>
      ))}
    </div>
  );
}

export default MarketList;