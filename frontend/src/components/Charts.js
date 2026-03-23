
import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

function Charts() {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/history?symbol=BTC&limit=20")
      .then(res => {
        const data = res.data.reverse();

        setChartData({
          labels: data.map(d => new Date(d.timestamp).toLocaleTimeString()),
          datasets: [
            {
              label: "BTC Price",
              data: data.map(d => d.price),
              borderColor: "blue"
            }
          ]
        });
      });
  }, []);

  return (
    <div>
      <h2>BTC Price Chart</h2>
      {chartData ? <Line data={chartData} /> : "Loading..."}
    </div>
  );
}

export default Charts;


