# Given an array of integers nums and an integer target, return indices of the two numbers such that they add
# up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def __init__(self, numbs, target):
        self.numbs = numbs
        self.target = target

    def TwoSums(self):
        """
        :type numbs: List[int]
        :type target: int
        :rtype: List[int]
        """

        prev = 0
        for i in self.numbs:
            for


lst = [1, 2, 3, 4]
solution = Solution(lst, 0)

solution.TwoSums()
