def simple_strategy(df):
    results = []

    for symbol, group in df.groupby("symbol"):
        group = group.sort_values("timestamp")

        if len(group) < 3:
            continue

        avg_price = group["price"].mean()
        latest_price = group.iloc[-1]["price"]

        signal = "HOLD"

        if latest_price > avg_price:
            signal = "BUY"
        elif latest_price < avg_price:
            signal = "SELL"

        results.append({
            "symbol": symbol,
            "signal": signal
        })

    return results