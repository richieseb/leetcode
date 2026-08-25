class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path, curr_sum):
            # If we have k numbers and the sum matches n, record the valid combination
            if len(path) == k:
                if curr_sum == n:
                    result.append(list(path))
                return
            
            # Pruning: if current sum exceeds n or we don't have enough numbers left
            if curr_sum > n or len(path) > k:
                return
            
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, curr_sum + i)
                path.pop()
                
        backtrack(1, [], 0)
        return result