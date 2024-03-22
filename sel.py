def troublesome_keys(key_counts):
    silly_key, quiet_key = None, None
    wrong_letter = None
    for key, count in key_counts.items():
        if count == 1 and key != 'q' and silly_key is None:
            silly_key = key
        elif count == 1 and key != silly_key and quiet_key is None:
            quiet_key = key
        elif quiet_key is not None:
            wrong_letter = key
    return silly_key, wrong_letter

# Example usage:
key_counts = {'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 2, 'q': 1}
print(troublesome_keys(key_counts))  # Output: ('b', 'c')