"""
Market Intelligence Engine

Coordinates the complete market scanning pipeline.
"""

from alpha.option_chain import OptionChain
from alpha.dynamic_window import DynamicWindow
from alpha.pair_ranker_v2 import PairRankerV2
from alpha.pair_selector import PairSelector


class MarketIntelligence:

    def __init__(self):

        self.option_chain = OptionChain()

    def scan(self):

        # --------------------------------------------------
        # Download latest option chain
        # --------------------------------------------------

        option_chain = self.option_chain.download()

        spot = option_chain["spot"]
        chain = option_chain["chain"]

        # --------------------------------------------------
        # Build dynamic strike window
        # --------------------------------------------------

        window_data = DynamicWindow.build(
            option_chain
        )

        valid_pairs = window_data["pairs"]

        # --------------------------------------------------
        # Rank every valid pair
        # --------------------------------------------------

        ranked = PairRankerV2.rank(
            valid_pairs,
            spot,
            chain,
        )

        # --------------------------------------------------
        # Select best opportunity
        # --------------------------------------------------

        best_pair = PairSelector.select(
            ranked
        )

        # --------------------------------------------------
        # Return complete market snapshot
        # --------------------------------------------------

        return {

            "spot": spot,

            "window_distance": window_data["distance"],

            "window": window_data["window"],

            "generated": window_data["generated"],

            "valid": window_data["valid"],

            "ranked": ranked,

            "best_pair": best_pair,
        }