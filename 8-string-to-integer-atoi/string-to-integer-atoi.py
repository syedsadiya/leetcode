class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        i = 0
        n = len(s)
        
        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        # Step 2: Determine sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # Step 3: Convert digits to integer
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
            
        result *= sign
        
        # Step 4: Handle 32-bit signed integer range bounds
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result