class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x not in ['+', '-', '*', '/']:
                stack.append(x)
            else:
                result = eval(stack[-2] + x + stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(int(result)))
        return int(stack[0])