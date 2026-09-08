class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #because both strings, when sorted, are equal, we can use a dict
        #key = sorted ver
        #value = string

        if sorted(s) == sorted(t):
            return(True)
        else:
            return(False)


