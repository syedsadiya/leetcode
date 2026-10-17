class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if the current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                # If we find the exact target, that's the closest possible sum
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum