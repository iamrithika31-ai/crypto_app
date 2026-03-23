import React from "react";
import MarketList from "./components/MarketList";
import Analytics from "./components/Analytics";
import Ranking from "./components/Ranking";
import Strategy from "./components/Strategy";
import Charts from "./components/Charts";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Crypto Dashboard</h1>

      <MarketList />
      <Analytics />
      <Ranking />
      <Strategy />
      <Charts />
    </div>
  );
}

export default App;