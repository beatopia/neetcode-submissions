class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort the strings
        if sorted(s) == sorted(t):
            return(True)
        else:
            return(False)
        #if the sorted versions are equal, return true
        #otherwise, false
