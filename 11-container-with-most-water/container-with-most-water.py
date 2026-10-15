class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Width between the two pointers
            width = right - left
            # Height is limited by the shorter line
            current_height = min(height[left], height[right])
            # Calculate area and update maximum
            max_water = max(max_water, width * current_height)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water