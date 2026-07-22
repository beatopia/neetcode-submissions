class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=0
        sorteds = sorted(s)
        sortedt = sorted(t)
        if sorteds == sortedt:
            return(True)
        else:
            return(False)
            