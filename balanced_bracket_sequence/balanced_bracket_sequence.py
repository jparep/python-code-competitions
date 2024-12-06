def isConvertibleData(dataset):
    result = []
    
    for s in dataset:
        # Check the counts of '(' and ')'
        open_count = s.count('(')
        close_count = s.count(')')
        
        # If the counts of '(' and ')' differ by more than 1, it's not possible to balance it in 1 move
        if abs(open_count - close_count) > 1:
            result.append(0)
            continue
        
        # Use a balance counter to simulate the bracket sequence
        balance = 0
        min_balance = 0
        
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            # Track the minimum balance during the traversal
            min_balance = min(min_balance, balance)
        
        # If min_balance >= -1 and final balance is 0, it's convertible
        if min_balance >= -1 and balance == 0:
            result.append(1)
        else:
            result.append(0)
    
    return result

# Example usage
dataset = [")(", "(()", "()"]
print(isConvertibleData(dataset))  # Output: [1, 0, 1]
