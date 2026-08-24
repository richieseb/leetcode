class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        
        for i, jump in enumerate(nums):
            # If the current index is past the maximum reachable index, we're stuck
            if i > max_reach:
                return False
            # Update the farthest index we can reach so far
            max_reach = max(max_reach, i + jump)
            
        return True