def sort_dicts_by_key(data, key, reverse=False):
    """AI-suggested: safely sort list of dicts by a given key, handling missing or mixed types."""
    if not isinstance(data, (list, tuple)):
        raise TypeError("data must be a list or tuple of dictionaries")
    
    def safe_key(d):
        """Ensure all keys are comparable (missing values replaced by None or 0)."""
        value = d.get(key)
        # Normalize all missing or non-numeric values to None
        if value is None:
            return float('-inf') if reverse else float('inf')  # missing keys go last or first
        return value

    try:
        return sorted(data, key=safe_key, reverse=reverse)
    except TypeError:
        raise ValueError(f"Cannot compare values for key '{key}'. Ensure consistent data types.")

if __name__ == "__main__":
    data = [
        {'name': 'alice'},
        {'name': 'bob', 'age': 25},
        {'name': 'carol', 'age': 28},
        {'name': 'david', 'age': 22}
    ]
    
    print(sort_dicts_by_key(data, 'age'))
