class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','*','/'}
        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                res = 0
                if token == '+':
                    res = num1 + num2
                elif token == '-':
                    res = num1 - num2                
                elif token == '*':
                    res = num1 * num2
                else:
                    res = int(num1 / num2)
                stack.append(res)
            
            else:
                stack.append(int(token))
            
        return stack[-1]


        