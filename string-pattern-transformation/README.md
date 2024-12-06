# Python Code Competition Problem: String Pattern Transformation

## Problem Statement
You are given a string `S` consisting of lowercase English letters and an integer `K`. Your task is to transform the string `S` using the following rules:

1. Divide `S` into consecutive non-overlapping substrings, each of length `K`. If the length of `S` is not a multiple of `K`, the last substring will contain the remaining characters.
2. For each substring:
   - Remove any duplicate characters, keeping only the first occurrence of each character in the substring.
3. Concatenate all processed substrings to form the final transformed string.

Write a function `transform_string(S: str, K: int) -> str` that performs this transformation and returns the resulting string.

---

## Input Format
- A single string `S` (1 ≤ len(S) ≤ 10⁴).
- An integer `K` (1 ≤ K ≤ len(S)).

---

## Output Format
- A single string representing the transformed string.

---

## Example Input
```plaintext
S = "aabbccddeeffgghh"
K = 4
