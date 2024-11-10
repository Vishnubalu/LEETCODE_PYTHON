"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.
    
    Example 1:
        Input: s = "()"
        Output: true
    
    Example 2:
        Input: s = "()[]{}"
        Output: true
    
    Example 3:
        Input: s = "(]"
        Output: false

    Example 4:
        Input: s = "([])"
        Output: true

    Constraints:
        1 <= s.length <= 104
        s consists of parentheses only '()[]{}'.
"""
def isValid(self, s: str) -> bool:
    open_brace = ["{", "(", "["]
    brace_hash = {"}" : "{", ")" : "(", "]" : "["}
    stack = []
    for sym in s:
        if sym in open_brace:
            stack.append(sym)
        else:
            if len(stack) == 0 or stack.pop() != brace_hash.get(sym):
                return False
    return True if len(stack) == 0 else False

print(isValid("([])"))