from alpha.market_intelligence import MarketIntelligence
from alpha.market_confirmation import MarketConfirmation

snapshot = MarketIntelligence().scan()

confirmation = MarketConfirmation.confirm(snapshot)

print("=" * 80)
print("MARKET CONFIRMATION")
print("=" * 80)

print("Signal     :", confirmation["signal"])
print("Confidence :", confirmation["confidence"])
print("Reason     :", confirmation["reason"])