"""
Feature Extraction
"""

from math import fabs


class FeatureExtractor:

    @staticmethod
    def extract(pair, spot):

        ce = pair["ce"]
        pe = pair["pe"]

        ce_strike = pair["ce_strike"]
        pe_strike = pair["pe_strike"]

        ce_spread = ce["top_ask_price"] - ce["top_bid_price"]
        pe_spread = pe["top_ask_price"] - pe["top_bid_price"]

        return {

            "ce_strike": ce_strike,
            "pe_strike": pe_strike,

            "distance_ce": fabs(spot - ce_strike),
            "distance_pe": fabs(spot - pe_strike),

            "ce_oi": ce["oi"],
            "pe_oi": pe["oi"],

            "min_oi": min(
                ce["oi"],
                pe["oi"],
            ),

            "ce_volume": ce["volume"],
            "pe_volume": pe["volume"],

            "min_volume": min(
                ce["volume"],
                pe["volume"],
            ),

            "ce_spread": ce_spread,
            "pe_spread": pe_spread,

            "total_spread": ce_spread + pe_spread,

            "ce_price": ce["last_price"],
            "pe_price": pe["last_price"],

            "ce_iv": ce["implied_volatility"],
            "pe_iv": pe["implied_volatility"],

            "ce_delta": ce["greeks"]["delta"],
            "pe_delta": pe["greeks"]["delta"],

            "ce_gamma": ce["greeks"]["gamma"],
            "pe_gamma": pe["greeks"]["gamma"],

            "ce_theta": ce["greeks"]["theta"],
            "pe_theta": pe["greeks"]["theta"],

            "ce_vega": ce["greeks"]["vega"],
            "pe_vega": pe["greeks"]["vega"],
        }