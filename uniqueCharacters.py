def is_unique_chars(st):
    if len(st) > 128:
        return False
    sorted_chars = sorted(st)
    prev_char = None
    for char in sorted_chars:
        if char == prev_char:
            return False
        prev_char == char
    return True
print(is_unique_chars("hello"))


