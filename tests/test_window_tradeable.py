from alpha.option_chain import OptionChain
from alpha.strike_selector import StrikeSelector

data = OptionChain().download()

selector = StrikeSelector(data)

window = selector.get_window(15)

count = 0

for strike in window:

    item = data["chain"][f"{strike:.6f}"]

    ce = item["ce"]
    pe = item["pe"]

    if (
        ce["oi"] > 0 and
        ce["volume"] > 0 and
        ce["last_price"] > 0 and
        ce["top_bid_price"] > 0 and
        ce["top_ask_price"] > 0 and
        pe["oi"] > 0 and
        pe["volume"] > 0 and
        pe["last_price"] > 0 and
        pe["top_bid_price"] > 0 and
        pe["top_ask_price"] > 0
    ):
        count += 1

print("Tradeable strikes in window:", count)