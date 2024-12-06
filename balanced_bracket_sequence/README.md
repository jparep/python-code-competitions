# Balanced Bracket Sequence

## Problem Statement

Given a dataset of strings containing only parentheses, characters `'('` and `')'`, the data represented by the string is valid if it is a balanced bracket sequence. One adjustment to the string can be made: at most one bracket can be moved from its original place to any other position in the string.

Your task is to determine whether, for each string, it is possible to balance the bracket sequence in **1 move or less**. Return an array of the size of the dataset, where the `i-th` integer is `1` if the string can be converted into a balanced string and `0` otherwise.

### Input Format

- An integer `n` (1 ≤ n ≤ 2 * 10⁵) – number of strings in the dataset.
- A list of strings `dataset[n]` where each string:
  - Contains only characters `'('` and `')'`.
  - Has a length `|dataset[i]|` (1 ≤ |dataset[i]| ≤ 2 * 10⁵).

### Output Format

Return a list of integers, where:
- `1` indicates the string can be converted into a balanced sequence in 1 move or less.
- `0` otherwise.

### Example Input

```python
n = 3
dataset = [")(", "(()", "()"]
