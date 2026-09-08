class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #given an array and a target number, return indices that will equal target
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i]+nums[j] == target:
                        return([i, j])

