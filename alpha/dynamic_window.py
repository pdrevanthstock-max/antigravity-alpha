"""
Dynamic Strike Window

Automatically expands the strike search window until
enough valid CE/PE pairs are available.
"""

from config.settings import (
    INITIAL_WINDOW,
    WINDOW_INCREMENT,
    MAX_WINDOW,
    MIN_VALID_PAIRS,
)

from alpha.strike_selector import StrikeSelector
from alpha.pair_generator import PairGenerator
from alpha.liquidity_filter import LiquidityFilter


class DynamicWindow:

    @staticmethod
    def build(option_chain):

        selector = StrikeSelector(option_chain)

        distance = INITIAL_WINDOW

        while distance <= MAX_WINDOW:

            window = selector.get_window(distance)

            pairs = PairGenerator.generate(
                window,
                option_chain["chain"],
            )

            valid_pairs, rejected_pairs = LiquidityFilter.filter(pairs)

            print("=" * 80)
            print(f"WINDOW ±{distance}")
            print("=" * 80)
            print(f"Generated : {len(pairs)}")
            print(f"Valid     : {len(valid_pairs)}")
            print()

            if len(valid_pairs) >= MIN_VALID_PAIRS:

                return {
                    "distance": distance,
                    "window": window,
                    "pairs": valid_pairs,
                    "generated": len(pairs),
                    "valid": len(valid_pairs),
                }

            distance += WINDOW_INCREMENT

        return {
            "distance": distance - WINDOW_INCREMENT,
            "window": window,
            "pairs": valid_pairs,
            "generated": len(pairs),
            "valid": len(valid_pairs),
        }