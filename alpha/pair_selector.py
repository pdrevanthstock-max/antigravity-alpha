"""
Pair Selector

Responsible for selecting the best candidate
from the ranked list.

No scoring.

No filtering.

No ranking.

Those responsibilities belong to
other modules.
"""


class PairSelector:

    @staticmethod
    def select(ranked_pairs):

        if not ranked_pairs:

            return None

        return ranked_pairs[0]

    @staticmethod
    def top(ranked_pairs, count=10):

        return ranked_pairs[:count]