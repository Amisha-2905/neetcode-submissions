class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        def backtr(o, c):
            if o == c and o == n:
                ans.append(''.join(stack))
            else:
                if c < o:
                    stack.append(')')
                    backtr(o ,c + 1)
                    stack.pop()
                    
                if o < n:
                    stack.append('(')
                    backtr(o + 1, c)
                    stack.pop()

        backtr(0,0)
        return ans
