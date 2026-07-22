class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortedlist = sorted(nums)
        for i in range(len(nums)-1):
            if sortedlist[i] == sortedlist[i+1]:
                return(True)
        return(False)