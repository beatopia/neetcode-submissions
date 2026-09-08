class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #use a set bc sets cannot have duplicates
        seen_numbers = set()
        for num in nums:
            if num in seen_numbers:
                return(True)
            seen_numbers.add(num)
        return(False)