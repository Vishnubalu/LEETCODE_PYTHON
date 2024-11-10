"""
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
        Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
        Return k.
    Custom Judge:

    The judge will test your solution with the following code:

        int[] nums = [...]; // Input array
        int[] expectedNums = [...]; // The expected answer with correct length

        int k = removeDuplicates(nums); // Calls your implementation

        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }

    If all assertions pass, then your solution will be accepted.

    Example 1:
        Input: nums = [1,1,2]
        Output: 2, nums = [1,2,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).

    Example 2:
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).

    Constraints:
        1 <= nums.length <= 3 * 104
        -100 <= nums[i] <= 100
        nums is sorted in non-decreasing order.
"""

from typing import List

# def removeDuplicates(nums: List[int]) -> int:
#     second_pointer = 1
#     first_pointer = 0
#     if len(nums) < 2:
#         return len(nums)
#     while second_pointer < len(nums):
#         if nums[first_pointer] < nums[second_pointer]:
#             if first_pointer + 1 != second_pointer:
#                 nums[first_pointer+1] = nums[second_pointer]
#             first_pointer += 1
#             second_pointer += 1
#         else:
#             second_pointer += 1
#     ans = first_pointer + 1
#     # while first_pointer + 1 < len(nums):
#     #     first_pointer += 1
#     #     nums[first_pointer] = "_"
#     return ans


def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        l = 1
        r = 1
        while r < len(nums):
            if nums[l-1] != nums[r]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l



num = [1, 2, 3, 3, 3, 4, 5, 5]
print(removeDuplicates(num))