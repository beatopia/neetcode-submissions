class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #array of strs, group all anagrams together in sublists
        #all anagrams share the same sorted ver we can use as key
        #key = sorted, values = unsorted

        anagrams = dict()
        

        for word in strs:
            count = [0]*26
            
            for char in word:
                index = ord(char) - ord('a')
                count[index]+=1
            key = tuple(count)

            #if sorted ver isnt a dict key, create one
            #then add it to the array


            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = []
                anagrams[key].append(word)
        return list(anagrams.values())