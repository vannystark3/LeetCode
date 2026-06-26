class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            l = len(stack)
            if l>0 and stack[-1]=='(' and p==')':
                stack.pop()
            elif l>0 and stack[-1]=='[' and p==']':
                stack.pop()
            elif l>0 and stack[-1]=='{' and p=='}':
                stack.pop()
            else:
                stack.append(p)
        return len(stack)==0