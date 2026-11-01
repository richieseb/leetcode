class Solution(object):
    def majorityElement(self, nums):
        element=0
        count=0
        for num in nums:
            if count==0:
                element=num
            if element==num:
                count+=1
            else:
                count-=1
        return element
