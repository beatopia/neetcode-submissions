class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            groups = {} #dict

            for word in strs:
                #key for dict is sorted word
                key = "".join(sorted(word))
                #if key isnt in dict yet, create it
                if key not in groups:
                    groups[key] = []
                
                #add word to corresponding dict
                groups[key].append(word)
            return(list(groups.values()))