#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best_val = None
    for key in a_dictionary:
        if best_val is None or a_dictionary[key] > best_val:
            best_val = a_dictionary[key]
            best_key = key
    return best_key
