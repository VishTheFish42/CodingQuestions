'''
PROBLEM 1.1
Is Unique

DESCRIPTION
Implement an algorithm to determine if a string has all unique characters.
'''

def is_unique(s):
  s_hash = {}
  
  for letter in s:
    if letter in s_hash:
      return False
    
    s_hash[letter] = 1
  
  return True

'''
ANALYSIS
Time Complexity: O(n)
Space Complexity: O(n)
'''

''''''''''''''''''''''''''''''''''''

'''
EXTENSION
What if you cannot use additional data structures?
'''

def is_unique2(s):
  s = ''.join(sorted(s))
  
  for i in range(len(s) - 1):
    if (s[i] == s[i + 1]):
      return False
  
  return True

'''
ANALYSIS
Time Complexity: O(n log n)
Space Complexity: O(n)
'''



def is_unique3(s):
  for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
      if (s[i] == s[j]):
        return False
  
  return True

'''
ANALYSIS
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
