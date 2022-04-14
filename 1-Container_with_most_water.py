class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        m = -9999
        while start <= end:
            f = height[start]
            g = min(height[start], height[end])
            h = end - start
            m = max(g * h, m)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return m
