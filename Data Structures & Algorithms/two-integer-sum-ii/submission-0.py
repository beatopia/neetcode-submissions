class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointers
        #if current_sum is less than target, move left pointer right
        #elif current_sum is more than target, move right pointer left
        current_sum = None
        pointer1, pointer2 = 0, len(numbers)-1
        while current_sum != target:
            current_sum = numbers[pointer1] + numbers[pointer2]
            if target < current_sum:
                pointer2-=1
            elif target > current_sum:
                pointer1+=1
        return[pointer1+1, pointer2+1]