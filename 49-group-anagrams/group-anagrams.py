from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        """
        d=defaultdict(list)
        for word in strs:
            lst=[0]*26
            for char in word:
                lst[ord(char)-ord('a')]+=1
            lst=tuple(lst)
            d[lst].append(word)
        return d.values()
