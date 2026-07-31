class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #STACK
        l1=['(','{','[']
        l2=[')','}',']']
        d=dict(zip(l2,l1))
        if s[0] in l2 or s[-1] in l1:
            return False

        ind=0
        result=[]
        while ind<len(s):
            if s[ind] in l1:
                result.append(s[ind])
            else:
                n=d[s[ind]]
                if len(result)>0 and result[-1]==n:
                    result.pop()
                else:
                    return False
            ind+=1
        if len(result)==0:
            return True
        else:
            return False       