def numbering(d, key_tuple):
    if key_tuple in d:
        base_key1, base_key2 = key_tuple
        i = 1
        new_key = (base_key1, f"{base_key2}_{i}")
        while new_key in d:
            i += 1
            new_key = (base_key1, f"{base_key2}_{i}")
        return new_key
    else:
        return key_tuple
