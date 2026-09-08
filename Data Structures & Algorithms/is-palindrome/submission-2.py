class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert our string to be case-insensitive and ignore non alphanum

        stripped_string = []
        for char in s:
            if char.isalnum() == True:
                stripped_string.append(char.lower())
        print(stripped_string)
        for i in range(len(stripped_string)//2):
            if stripped_string[i] != stripped_string[-(i+1)]:
                print(stripped_string[i], stripped_string[-i+1])
                return False
        return True
