class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        output = []
        prefix_product = 1
        suffix_product = 1
        for i in range(len(nums)):
            prefix.append(prefix_product)
            prefix_product*=nums[i]
            
        for i in range(len(nums)-1, -1, -1):
            suffix.append(suffix_product)
            suffix_product *= nums[i]
        suffix.reverse()

        for i in range(len(nums)):
            if i != 0:
                output.append(prefix[i]*suffix[i])
            else:
                output.append(suffix[i])
        return(output)
        



        