class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer=[]
        for i in range(len(nums)-1):
            for x in range(len(nums)):
                print(nums[i])
                print(nums[x])
                if (nums[i]+nums[x]) == target and i != x:
                    answer.append(i)
                    answer.append(x)
                    return(answer)
                    