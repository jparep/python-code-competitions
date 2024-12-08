def longest_palindromic_substring_center(s):
    if not s:
        return ""

    def expand_around_center(left, right):
        # Expand as long as the characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindromes (single character center)
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

        # Even-length palindromes (two-character center)
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

# Test cases
print(longest_palindromic_substring_center("babad"))  # Output: "bab" or "aba"
print(longest_palindromic_substring_center("cbbd"))   # Output: "bb"
print(longest_palindromic_substring_center("a"))      # Output: "a"
print(longest_palindromic_substring_center("ac"))     # Output: "a" or "c"
