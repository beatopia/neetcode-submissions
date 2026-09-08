class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped=""
        for char in s:
            if char.isalnum():
                stripped+=char.lower()

        for i in range(len(stripped) // 2):
            if stripped[i] != stripped[-(i+1)]:
                return(False)
        return(True)
