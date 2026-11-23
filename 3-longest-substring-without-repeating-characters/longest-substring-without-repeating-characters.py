class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        best=0
        seen=set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[start])
                start+=1
            seen.add(s[i])
            best=max(best,i-start+1)
        return best
            
