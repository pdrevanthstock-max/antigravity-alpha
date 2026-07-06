from alpha.option_chain import OptionChain
from alpha.dynamic_window import DynamicWindow

result = DynamicWindow.build(
    OptionChain().download()
)

print("=" * 80)
print("FINAL RESULT")
print("=" * 80)

print("Window Size :", result["distance"])
print("Generated   :", result["generated"])
print("Valid       :", result["valid"])

print()

print("Strike Window")

for strike in result["window"]:
    print(strike)