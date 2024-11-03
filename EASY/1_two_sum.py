from collections import defaultdict
from math import inf


class Solution(object):
    def twoSum(self, nums, target):
        """_summary_
        Args:
            nums (List[int]): list of integers
            target (int): target
        Return:
            List[int]: index of the numbers which sum = target
        """
        hashmap = {}
        for ind, value in enumerate(nums):
            if hashmap.get(target-value, -1) != -1:
                return [hashmap[target-value], ind]
            hashmap[value] = ind
            
sol = Solution().twoSum([2, 7, 11, 15], 9)
print(sol)
        