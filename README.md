# Crypto Dashboard

A full-stack crypto market data & analytics dashboard built with **FastAPI**, **SQLite**, **SQLAlchemy**, **Pandas**, and **React**. This project fetches crypto prices, performs analytics, runs a simple trading strategy, and visualizes historical price charts.

---

## Features

- Fetches live cryptocurrency data using the [CoinGecko API](https://www.coingecko.com/en/api)
- Stores market data in a local SQLite database
- Computes analytics like price and volume changes
- Runs a simple strategy based on average price
- Displays:
  - Market data table
  - Analytics summary
  - Strategy signals
  - Historical price chart (Chart.js + React)

---

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, SQLite, Pandas, Requests
- **Frontend:** React, Axios, Chart.js, react-chartjs-2
- **APIs:** REST endpoints for fetching, analytics, and strategy

---

## Project Structure


    crypto_app/
├─ backend/
│  ├─ main.py
│  ├─ models.py
│  ├─ database.py
│  ├─ fetch_data.py
│  ├─ analytics.py
│  ├─ strategy.py
│  └─ requirements.txt
├─ frontend/
│  ├─ package.json
│  ├─ src/
│  │  ├─ App.js
│  │  ├─ index.js
│  │  └─ components/
│  │     ├─ MarketList.js
│  │     ├─ Analytics.js
│  │     ├─ Strategy.js
│  │     ├─ Ranking.js
│  │     └─ Charts.js
└─ README.md



## Frontend Output
![Frontend Screenshot](frontend/screenshots/frontend_output.png)

This shows the React frontend displaying market data, analytics, and charts.

http://localhost:3000

---

## Backend Output
![Backend Screenshot](backend/screenshots/backend_output.png)

This shows the FastAPI backend logs and API response output.

http://127.0.0.1:8000/docs