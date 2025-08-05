# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
class Solution: #day 1
    def isAnagram(self, s: str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
    
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
from typing import List #day 2
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
class Solution:
    def hasDuplicate(self, nums:List[int]) -> bool:
        return len(nums) != len(set(nums))
    
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.
from typing import List #day 4

class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

