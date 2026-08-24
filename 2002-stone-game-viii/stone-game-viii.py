class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        
        # Manually compute prefix sums
        prefix = [0] * n
        current_sum = 0
        for i in range(n):
            current_sum += stones[i]
            prefix[i] = current_sum
        
        # dp[i] represents the maximum score difference the current player 
        # can get when considering choices starting from index i.
        dp = [-float('inf')] * n
        
        # Base case: When only two stones are effectively left, 
        # the player must take all remaining stones (the entire prefix sum).
        dp[n - 2] = prefix[-1]
        
        # Work backwards from n - 3 down to 0
        for i in reversed(range(n - 2)):
            dp[i] = max(dp[i + 1], prefix[i + 1] - dp[i + 1])
            
        return dp[0]
        