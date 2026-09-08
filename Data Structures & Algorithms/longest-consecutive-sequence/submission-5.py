class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we can use a set because we dont care about duplicates
        nums = set(nums)
        #for each num, if it doesnt have a left neighbor, we know its the start of a streak
        #if num+1 exists, streak+=1
        #if num+1 doesnt exist, streak=1 go to next number
        max_streak = 0
        for num in nums:
            streak = 1
            on = True
            current_num = num
            if num-1 not in nums:
                #if left neighbor doesnt exist, start of streak
                #check if num+1 exists, if its does iterate streak
                while 1:
                    if current_num+1 in nums:
                        streak+=1
                        current_num+=1
                    else:
                        break
            if streak > max_streak:
                max_streak = streak
        return(max_streak)
