class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nums1=nums2=res=arr[0]
        for num in arr[1:]:
            if nums1<0:
                nums1=0
            if num>=0:
                nums1+=num
            else:
                nums1=max(nums1+num,nums2)
            if nums2<0:
                nums2=0

            nums2+=num
            res=max(nums1,nums2,res)
        return res

        