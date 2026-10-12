class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #array of strs, group all anagrams together in sublists
        #all anagrams share the same sorted ver we can use as key
        #key = sorted, values = unsorted

        anagrams = dict()

        for word in strs:
            #if sorted ver isnt a dict key, create one
            #then add it to the array
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = []
                anagrams[sorted_word].append(word)
        return list(anagrams.values())