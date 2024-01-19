"""
Minimum Number of Steps to Make Two Strings Anagrams 

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 

"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = {}

        for char in s: 
            s_freq[char] = s_freq.get(char, 0) + 1

        for char in t: 
            if char in s_freq:
                s_freq[char] = s_freq.get(char) - 1
                if s_freq[char] == 0: 
                    del s_freq[char]

        if not s_freq: 
            return 0 
        
        return sum(v for k, v in s_freq.items())
