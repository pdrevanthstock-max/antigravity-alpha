"""
Market Confirmation

Determines whether current market conditions
support taking the highest-ranked opportunity.
"""


class MarketConfirmation:

    @staticmethod
    def confirm(snapshot):

        spot = snapshot["spot"]

        best = snapshot["best_pair"]

        if best is None:

            return {
                "signal": "NO_TRADE",
                "confidence": 0.0,
                "reason": "No valid option pair",
            }

        pair = best["pair"]

        ce = pair["ce_strike"]

        pe = pair["pe_strike"]

        if spot > ce:

            return {
                "signal": "BULLISH",
                "confidence": 0.50,
                "reason": "Spot above CE strike",
            }

        if spot < pe:

            return {
                "signal": "BEARISH",
                "confidence": 0.50,
                "reason": "Spot below PE strike",
            }

        return {
            "signal": "SIDEWAYS",
            "confidence": 0.25,
            "reason": "Spot between selected strikes",
        }