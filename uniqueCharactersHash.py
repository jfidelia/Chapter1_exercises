def isUnique(str):
    if len(str) > 256:
        return False
    else:
        dict = {}

        for s in str:
            if (s in dict.keys()) == False:
                dict[s] = True
            else:
                return False
    return True

str = input("enter string")
print(isUnique(str))