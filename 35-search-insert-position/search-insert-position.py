class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        while(i<len(nums) and target>nums[i]):
            if(nums[i]==target):
                return i
            else:
                i+=1
        return i