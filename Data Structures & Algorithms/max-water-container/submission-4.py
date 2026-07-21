class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # diff = (taller - shorter) * index_distance 
        # area = taller * index_distance - diff
        area = 0
        for i in range(len(heights)):
            l, r = i, i + 1
            while r < len(heights):
                diff = abs(heights[r] - heights[l]) * (r - l)
                if heights[l] > heights[r]:
                    taller = heights[l]
                else:
                    taller = heights[r]
                curr_area = taller * (r - l) - diff
                area = curr_area if curr_area > area else area
                r += 1
        return area