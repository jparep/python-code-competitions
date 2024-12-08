# Problem: Longest Palindromic Substring

### Description
Find the longest substring in a given string that is a palindrome.

### Examples

#### Example 1
- Input: `"babad"`
- Output: `"bab"`
  - Note: `"aba"` is also a valid answer.

#### Example 2
- Input: `"cbbd"`
- Output: `"bb"`

### Constraints
1. The input string's length will not exceed 1000.
2. Only lowercase English letters are allowed.

### Goal
Write a Python function `longest_palindromic_substring(s)` that returns the longest palindromic substring of the given string `s`.



# Problem: Optimized Longest Palindromic Substring (Center Expansion)

### Description
Find the longest substring in a given string that is a palindrome using the center-expansion technique for optimization.

### Examples

#### Example 1
- Input: `"babad"`
- Output: `"bab"`
  - Note: `"aba"` is also a valid answer.

#### Example 2
- Input: `"cbbd"`
- Output: `"bb"`

### Constraints
1. The input string's length will not exceed 1000.
2. Only lowercase English letters are allowed.

### Goal
Write a Python function `longest_palindromic_substring_center(s)` that:
1. Expands around the center of possible palindromes.
2. Returns the longest palindromic substring of the given string `s`.
