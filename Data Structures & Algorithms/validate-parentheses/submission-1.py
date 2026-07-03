class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_set = {'(', '{', '['}
        closed_set = {')', '}', ']'}
        close_dict = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in open_set:
                stack.append(c)
            elif c in closed_set:
                if stack:
                    last = stack[-1]
                    if close_dict[last] == c:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if stack:
            return False
        
        return True

