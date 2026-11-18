class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(path: list[int], options: list[int]):
            if not options:
                res.append(list(path))
                return
            
            for i in range(len(options)):
                path.append(options[i])
                backtrack(path, options[:i] + options[i + 1:])
                path.pop()
                
        backtrack([], nums)
        return res