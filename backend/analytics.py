import pandas as pd

def compute_analytics(df):
    results = []

    for symbol, group in df.groupby("symbol"):
        group = group.sort_values("timestamp")

        if len(group) < 2:
            continue

        price_change = ((group.iloc[-1]["price"] - group.iloc[0]["price"]) / group.iloc[0]["price"]) * 100
        volume_change = ((group.iloc[-1]["volume"] - group.iloc[0]["volume"]) / group.iloc[0]["volume"]) * 100

        results.append({
            "symbol": symbol,
            "price_change_pct": round(price_change, 2),
            "volume_change_pct": round(volume_change, 2)
        })

    results = sorted(results, key=lambda x: x["price_change_pct"], reverse=True)

    for i, r in enumerate(results):
        r["rank"] = i + 1

    return results