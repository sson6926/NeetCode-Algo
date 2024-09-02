class Solution:
    def isValid(self ,s: str) -> bool:
        cap_ngoac = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for x in s:
            if x in cap_ngoac.keys():
                stack.append(x)
            elif x in cap_ngoac.values():
                if not stack or x != cap_ngoac[stack[-1]]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
