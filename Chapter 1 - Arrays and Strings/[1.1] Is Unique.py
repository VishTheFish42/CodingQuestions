'''
PROBLEM 1.1
Is Unique

DESCRIPTION
Implement an algorithm to determine if a string has all unique characters.

ASSUMPTIONS MADE
[1] An empty string does have all unique characters (because there is no possibility of finding duplicate characters in an empty string).
'''

def is_unique(s):
  s_hash = {}
  
  for letter in s:
    if letter in s_hash:
      return False
    
    s_hash[letter] = 1
  
  return True

'''
EXTENSION
[1] First, we sort the string.
[2] Once the string is sorted, duplicate characters can only appear next to one another, so we check each element and its immediate successor. 
    If they are the same, we can return False.
[3] Otherwise, we return True once the loop has completed.
[4] Due to efficient sorting, time complexity is improved. Explicitly, we are not using an additional data structure. 
    Under the hood, though, using sorted like this actually causes Python to create an additional list, sort it, and rejoin it, making the space complexity the same as before.

ANALYSIS
Time Complexity: O(n)
Space Complexity: O(n)
'''

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
EXPLANATION
[1] We iterate across each letter in the input string s. If the letter exists as a key in s_hash, then we can return False because that letter has already been used. If not, we add a new key-value pair to s_hash: the key is the new letter, and the value is just 1.
[2] We can simply return True at the end because exiting the loop must mean that we never returned False.
[3] We use a hash table here to keep lookup at O(1), thereby increasing the efficiency.

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
EXPLANATION
[1] We have two pointers that iterate across the string. One iterates from the first character to the second to last character, 
    and the other iterates from 1 ahead of the current position of the first pointer to the last character.
[2] If the characters at the two pointers match, then we can return False since there is no way for all characters to be unique.
[3] If the loop exits, we can return True, since there are no two matching characters.

ANALYSIS
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
