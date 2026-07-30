class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref=strs[0]
        for i in strs:
            if(len(pref)>len(i)):
                pref=i
        l=len(strs)
        count=0
        result=" "
        while(l!=count):
            count=0
            for i in strs:
                if(pref==i[:len(pref)]):
                    count+=1
            result=pref
            pref=pref[:-1]
        if(l==count):
            return result