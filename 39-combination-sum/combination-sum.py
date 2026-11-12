class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        
        def backtrack(start: int, path: list[int], current_sum: int):
            if current_sum == target:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                if current_sum + num > target:
                    break
                path.append(num)
                backtrack(i, path, current_sum + num)
                path.pop()
                
        backtrack(0, [], 0)
        return res