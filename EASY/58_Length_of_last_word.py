
"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.
Example 2:
    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: The last word is "moon" with length 4.
Example 3:
    Input: s = "luffy is still joyboy"
    Output: 6
    Explanation: The last word is "joyboy" with length 6.
    
Constraints:
    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""

def lengthOfLastWord(self, s: str) -> int:
    n = len(s)
    ans = ""
    for i in range(n-1, -1, -1):
        if s[i] != " ":
            ans = s[i] + ans
        else:
            if len(ans) > 0:
                return len(ans)
    return len(ans)


# Pythonic way

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return (len(s.strip().split(' ')[-1]))