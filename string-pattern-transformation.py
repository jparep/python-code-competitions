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