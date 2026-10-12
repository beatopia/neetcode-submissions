class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #array of strs, group all anagrams together in sublists
        #all anagrams share the same sorted ver we can use as key
        #key = sorted, values = unsorted
        anagrams = dict()
        
        for word in strs:
            #make count 1-26 list, make sure its 0 so we can iterate
            count = [0]*26
            #for each char in word
            for char in word:
                index = ord(char) - ord("a")
                count[index]+=1
            key = tuple(count)
            #find index of char (1-26) using ord
            #iterate that index in count
            #turn count into a tuple bc we cant use 
            
            

            #if key isnt a dict key alr, create one (otherwise error)
            #then add it to the array
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = []
                anagrams[key].append(word)
        return list(anagrams.values())