class Solution:

#Plan: str1: "leet" str2: "code"
# encoded ver: 4#leet4#code
# header is num of char in string and #

#given list of strings, output single string
    def encode(self, strs: List[str]) -> str:
        #for each string, add len of string and # to the front
        encoded_string = ""
        for string in strs:
            encoded_string = encoded_string+((str(len(string))+"#")+string)
        return(encoded_string)
        
    def decode(self, s: str) -> List[str]:
        #example: 4#meow10#onemillion
        count="" #how many chars
        current=0 #current pos
        decoded_strs = []
        current_sentence=""
        while current < len(s):
            while s[current] != "#":
                #if s hasn't found # yet, we're still decoding string length
                count+=str(s[current])
                current+=1
            for length in range(int(count)):
                current_sentence+=(str(s[length+current+1]))
            current=current+int(count)+1
            decoded_strs.append(current_sentence)
            current_sentence = ""
            count=""
        return(decoded_strs)

                
                




