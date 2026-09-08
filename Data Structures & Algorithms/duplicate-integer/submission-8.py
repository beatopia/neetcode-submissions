class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        #if making an empty set specifically, use set(), as {} means empty dict
        for num in nums:
            if num in seen:
                return(True)
            seen.add(num) #append is for ordered
        return(False)
