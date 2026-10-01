from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        for i in s:
            if i=='{' or i=='[' or i=='(':
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if i==']' and top!='[':
                    return False
                elif i=='}' and top!='{':
                    return False
                elif i==')' and top!='(':
                    return False
        return len(stack)==0          
