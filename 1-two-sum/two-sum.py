class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i, value in enumerate(nums):
            num=target-value
            if num in d:
                return [d[num],i]
            else:
                d[value]=i
        return []
                               