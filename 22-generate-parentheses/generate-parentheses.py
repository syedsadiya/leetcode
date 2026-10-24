class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # If the current string has reached the maximum length (2 * n), add it to results
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
                
            # We can add an opening bracket if we haven't used all n of them yet
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # We can add a closing bracket only if it won't exceed the number of opening brackets
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return result