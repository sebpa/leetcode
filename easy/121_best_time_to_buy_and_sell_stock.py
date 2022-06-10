# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_min_price = prices[0]
        for price in prices[1:]:
            if price < current_min_price:
                current_min_price = price
            if price - current_min_price > max_profit:
                max_profit = price - current_min_price
        return max_profit
