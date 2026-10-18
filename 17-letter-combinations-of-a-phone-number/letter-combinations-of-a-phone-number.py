class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current_path: list):
            # If the current path is the same length as digits, we have a complete combination
            if index == len(digits):
                result.append("".join(current_path))
                return
                
            # Get the letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            
            for letter in possible_letters:
                # Add the letter to our current path
                current_path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, current_path)
                # Backtrack by removing the letter before trying the next one
                current_path.pop()
                
        backtrack(0, [])
        return result