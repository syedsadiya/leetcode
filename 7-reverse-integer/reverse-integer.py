class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Keep track of the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        
        # Convert to string, reverse it, and convert back to integer
        reversed_x = int(str(abs(x))[::-1]) * sign
        
        # If reversing x causes the value to go outside the signed 32-bit integer range, return 0
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
            
        return reversed_x