def transform_string(S: str, K: int) -> str:
    """Transform string into substring and remove duplicate. Concate the substring to main string"""
    
    # Use an order set to retain unque charactors
    def remove_duplicate(substring: str) -> str:
        seen = set()
        result = []
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)
    
    chunks = [S[i: i+K] for i in range(0, len(S), K)]
    
    processed_chunks = [remove_duplicate(chunk) for chunk in chunks]
    
    return ''.join(processed_chunks)

# Example usage
S = 'aabbccddeeffggh'

K = 4
result = transform_string(S, K)
print(result)



############################################
#    OPTIMIZED APPROACH 
############################################
def isConvertibleData(dataset):
    def can_balance(s):
        balance = 0
        min_balance = 0

        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            
            # Track the lowest balance
            min_balance = min(min_balance, balance)
            
            # Early termination: If the imbalance is already too high, return 0
            if min_balance < -1:
                return 0

        # Check if the final balance is zero
        return 1 if balance == 0 else 0

    # Process each string in the dataset
    return [can_balance(s) for s in dataset]
