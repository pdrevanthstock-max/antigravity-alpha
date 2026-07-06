from alpha.option_chain import OptionChain

data = OptionChain().download()

chain = data["chain"]

count = 0

for strike, item in chain.items():

    ce = item["ce"]
    pe = item["pe"]

    if (
        ce["oi"] > 0 and
        pe["oi"] > 0 and
        ce["volume"] > 0 and
        pe["volume"] > 0
    ):
        count += 1

print("=" * 80)
print("STRIKES WITH BOTH SIDES TRADEABLE")
print("=" * 80)
print(count)