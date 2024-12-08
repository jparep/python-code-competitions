def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""

    # Initialize a DP table
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substring of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for substrings longer than 2
    for length in range(3, n + 1):  # length is the current substring length
        for i in range(n - length + 1):
            j = i + length - 1  # Endpoint of the substring
            if s[i] == s[j] and dp[i + 1][j - 1]:  # Expand if inner substring is palindrome
                dp[i][j] = True
                start = i
                max_length = length

    # Extract the longest palindrome
    return s[start:start + max_length]

# Test cases
print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"
print(longest_palindromic_substring("cbbd"))   # Output: "bb"
