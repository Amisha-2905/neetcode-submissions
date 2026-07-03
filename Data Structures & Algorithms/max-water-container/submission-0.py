class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = (j - i) * min(heights[i], heights[j])
        while i < j:
            new_area = (j - i) * min(heights[i], heights[j])
            if new_area > max_area:
                max_area = new_area
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
                j -= 1
        
        return max_area

