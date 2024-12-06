def transform_string(S: str, K: int) -> str:
    """Transform string into substring and remove duplicate. Concate the substring to main string"""
    
    # Use an order set to retain unque charactors
    def remove_duplicate(substring: str) -> str:
        