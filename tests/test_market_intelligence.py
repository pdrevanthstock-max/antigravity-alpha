from alpha.market_intelligence import MarketIntelligence


engine = MarketIntelligence()

result = engine.scan()

print("=" * 80)
print("MARKET SUMMARY")
print("=" * 80)

print("Spot            :", result["spot"])
print("Window Distance :", result["window_distance"])
print("Generated       :", result["generated"])
print("Valid           :", result["valid"])

print()

print("=" * 80)
print("BEST PAIR")
print("=" * 80)

best = result["best_pair"]

if best is None:

    print("No valid pair found.")

else:

    pair = best["pair"]

    print(
        f"CE {pair['ce_strike']}  <->  "
        f"PE {pair['pe_strike']}"
    )

    print(f"Score : {best['score']:.4f}")

    print()

    print("=" * 80)
    print("TOP 10 RANKED PAIRS")
    print("=" * 80)

    for item in result["ranked"][:10]:

        pair = item["pair"]

        print(
            f"CE {pair['ce_strike']}  <->  "
            f"PE {pair['pe_strike']}    "
            f"Score = {item['score']:.4f}"
        )