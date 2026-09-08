class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped=""
        for char in s:
            if char.isalnum() == True:
                stripped+=char.lower()
        
        for i in range(len(stripped)//2):
            #for i in length divided by 2, rounded down
            if stripped[i] != stripped[-(i+1)]:
                return(False)
        return(True)   


        #if our string is alphanumeric
            
                
