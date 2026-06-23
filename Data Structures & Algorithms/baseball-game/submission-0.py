class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for op in operations:
            n = len(ans)
            if op == '+':
                a = ans[n - 1]
                b = ans[n - 2]
                ans.append(int(a + b))
            elif op == 'D':
                a = ans[n - 1]
                ans.append(int(2 * a))
            elif op == 'C':
                ans = ans[:-1]
            else:
                ans.append(int(op))
        
        an = 0
        for anss in ans:
            an += anss
        
        return an