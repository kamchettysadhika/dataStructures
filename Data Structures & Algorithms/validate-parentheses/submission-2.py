class Solution:
    def isValid(self, s: str) -> bool:
        #closing paranthese is going to maytch teh most recent opening parantgese 
        # LAST SEEN -> STACK 
        #so we add everything to the stack and once we see a closing paranthese it should be that of the last seen opening paranthese 
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closeToOpen: 
                if stack and stack[-1]== closeToOpen[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        return stack == []