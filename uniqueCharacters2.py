def is_unique_chars(str):
    arr = [False] * 128
    for char in str:
        index = ord(char)
        if arr[index]:
            return False
        else:
            arr[index] = True
    return True

print(is_unique_chars("yelp"))