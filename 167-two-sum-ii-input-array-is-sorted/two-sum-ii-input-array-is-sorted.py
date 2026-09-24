class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0,len(numbers)-1
        while l<r:
            sums=numbers[l]+numbers[r]
            if sums==target:
                return [l+1,r+1]
            elif sums<target:
                l+=1
            else:
                r-=1

        