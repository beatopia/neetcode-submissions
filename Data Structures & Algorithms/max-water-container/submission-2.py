class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        cur_max = 0
        while left != right:
            height = min(heights[left], heights[right])
            width = right-left
            area = width*height
            if area > cur_max:
                cur_max = area
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return(cur_max)