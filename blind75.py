# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
class Solution: #day 1
    def isAnagram(self, s: str, t:str) -> bool:
        if len(s) != len(t):# checks if s and t have the same length
            return False #false if they don't match
        
        return sorted(s) == sorted(t) #rearranges the characters in both strings and checks if they are equal. if equal yes its an anagram, otherswise return false
    
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
#hash map solution(one pass)
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

#hash map solution(two pass)
class Solution:
    def twoSum(seld, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            seen[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen and seen[diff] != i:
                return [i, seen[diff]]
#valid palindrome
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# A palindrome is a string that reads the same forward and backward.
class Solution: #day 5
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        return newStr == newStr[::-1]

def isPalindrome(self, s:str) -> bool:
    l, r = 0, len(s) - 1 #l starts at the beginning, r starts at the end. two pointers that move toward each other
    while l < r: #keep checking as long as l left pointer is strictly before r right pointer
        while l < r and not self.alphaNum(s[l]):
            l += 1 #if l is not a no or letter move it forward l += 1
        while l < r and not self.alphaNum(s[r]):
            r -= 1 #if r is not a no or letter move it backward r-= 1
        if s[l].lower() != s[r].lower(): #compare the charcters and convert to lowercase
            return False #if they are different the string is not a palindrome
        l, r = l + 1, r - 1 #move the pointers Toward each other; left forward and right backward. shrinking window continues until l>=r
    return True #no matched characters found, so it is a palindrome
#helper function to check if a character is alphanumeric
def alphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))