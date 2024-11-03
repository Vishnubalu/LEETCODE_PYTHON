from typing import List

"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

def longestCommonPrefix(strs: List[str]) -> str: 
    
    smallest_ind = 0
    for ind, s in enumerate(strs):
        if ind == 0:
            s_str = len(s) 
        if len(s) < s_str:
            smallest_ind = ind
            s_str = len(s)
    ans = ""
    small_str = strs[smallest_ind]
    for i in range(len(small_str)):
        v = small_str[i]
        value_flag = True
        for s in strs:
            if s[i] != v:
                value_flag = False
                break
        if value_flag:
            ans += v
    return ans

#     hash_map = {}
#     for ind, s in enumerate(strs[smallest_ind]):
#         if ind < len(strs[smallest_ind]) - 1:
#             hash_map[s] = strs[smallest_ind][ind+1]
#         if len(strs[smallest_ind]) == 1:
#             hash_map[s] = strs[smallest_ind]
    
#     final_resutl = ""
#     for s in strs:
#         prefix=""
#         for ind, c in enumerate(s):
#             if prefix == "" and hash_map.get(c, -1) != -1:
#                 prefix += c
#             elif hash_map.get(s[ind-1]) == c:
#                 prefix += c
#             else:
#                 if len(prefix) > 0:
#                     final_resutl = prefix
#                 prefix = ""
#     return final_resutl
                
                
print(longestCommonPrefix(["ab", "a"]))
