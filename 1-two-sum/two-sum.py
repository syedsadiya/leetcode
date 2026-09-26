class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is already in our dictionary
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, store the current number and its index
            num_map[num] = i
            
        return []