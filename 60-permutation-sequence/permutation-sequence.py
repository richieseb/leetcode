class Solution(object):
    def getPermutation(self, n, k):
        numbers=range(1,n+1)
        per=''
        k-=1
        while n>0:
            n-=1
            index,k=divmod(k,math.factorial(n))
            per+=str(numbers[index])
            numbers.remove(numbers[index])
        return per