class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        
        def backtrack(start: int, path: list[int], current_sum: int):
            if current_sum == target:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same tree level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                num = candidates[i]
                if current_sum + num > target:
                    break
                    
                path.append(num)
                backtrack(i + 1, path, current_sum + num)
                path.pop()
                
        backtrack(0, [], 0)
        return res