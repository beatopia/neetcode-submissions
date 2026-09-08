class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we use a dict because each group of anagrams will have a sorted version in common
        #that we can use as a key to sort them into groups
        group = {}
        #for each word, check if it has a key in the dict alr
        #so we have to make the key first
        for word in strs:
            key = "".join(sorted(word))
            #if it doesnt, make one
            if key not in group:
                group[key] = []
            group[key].append(word)
        #then add the word to the dict in its correct "group"
        

        return(list(group.values()))
        
