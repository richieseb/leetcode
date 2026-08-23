class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort() # Sort to easily skip duplicates
        
        def dfs(start, cur, total):
            if total == target:
                res.append(list(cur))
                return
            if total > target:
                return 
                
            for i in range(start, len(candidates)):
                # Skip duplicates if they appear at the same tree level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # Pruning: since array is sorted, if total exceeds target, future elements will too
                if total + candidates[i] > target:
                    break
                    
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop() # Backtrack
                
        dfs(0, [], 0)
        return res