'''
PROBLEM 1.2
Check Permutation

DESCRIPTION
Given two strings, write a method to decide if one is a permutation of the other.
'''

from collections import Counter

def check_permutation(s1, s2):
  if (len(s1) != len(s2)):
    return False

  s1_hash = Counter(s1)
  
  for letter in s2:
    if (s1_hash[letter] == 0):
      return False

    s1_hash[letter] -= 1

  return True

'''
ANALYSIS
Time Complexity: O(n)
Space Complexity: O(c)
where n is the length of s1 and s2, and c is the number of unique characters in s1
'''
