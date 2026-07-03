class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack:
                top = stack[-1]
                if temp > top[1]:
                    stack.pop()
                    ans[top[0]] = i - top[0]
                else:
                    break
            
            stack.append([i, temp])
        
        return ans