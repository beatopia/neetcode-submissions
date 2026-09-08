class Solution:
    def findMin(self, nums: List[int]) -> int:
        found = False
        left = 0
        right = len(nums)-1
        if nums[left] < nums[right]:
            cur_smallest = nums[left]
        else:
            cur_smallest = nums[right]
        
        if len(nums) == 1:
            return(nums[0])
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        while found != True:
            if nums[left] > nums[left+1]:
                left+=1
                if nums[left] < cur_smallest:
                    cur_smallest = nums[left]
            elif nums[right] > nums[right-1]:
                right-=1
                if nums[right] < cur_smallest:
                    cur_smallest = nums[right]
            else:
                return(cur_smallest)
                found = True
