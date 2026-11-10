class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def backtrack(index,path):
            if len(nums)==index:
                result.append(path[:])
                return 

            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()
            backtrack(index+1,path)
        backtrack(0,[])
        return result