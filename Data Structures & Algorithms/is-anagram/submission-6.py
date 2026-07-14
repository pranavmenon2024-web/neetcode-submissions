class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #early exit for differing length
        if len(s)!=len(t):
            return False
        #building hashmap for first pass
        check={}
        for c in s:
            if c in check:
                check[c]+=1
            else:
                check[c]=1
        #comparing second string to first
        for c in t:
            if c not in check or check[c]<0:
                return False
            else:
                check[c]-=1
        #check if hashmap values are nonzero
        for value in check.values():
            if value!=0:
                return False
        return True