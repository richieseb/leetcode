class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max=float('-inf')
        max_sum=float('-inf')
        cur_min=float('inf')
        min_sum=float('inf')
        tot=0
        for i in nums:
            cur_max=max(i,i+cur_max)
            max_sum=max(cur_max,max_sum)

            cur_min=min(i,cur_min+i)
            min_sum=min(min_sum,cur_min)

            tot+=i
        return max(max_sum,tot-min_sum) if max_sum>0 else max_sum