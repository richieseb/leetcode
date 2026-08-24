class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)
        dp = [[-float('inf')] * 3 for _ in range(k + 1)]
        dp[0][0] = 0
        for price in prices:
            next_dp = [row[:] for row in dp]
            for j in range(k + 1):
                if j < k:
                    next_dp[j + 1][1] = max(next_dp[j + 1][1], dp[j][0] - price)
                    next_dp[j + 1][2] = max(next_dp[j + 1][2], dp[j][0] + price)
                if dp[j][1] != -float('inf'):
                    next_dp[j][0] = max(next_dp[j][0], dp[j][1] + price)
                if dp[j][2] != -float('inf'):
                    next_dp[j][0] = max(next_dp[j][0], dp[j][2] - price)
            dp = next_dp
        return max(dp[j][0] for j in range(k + 1))