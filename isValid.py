def isValid(s):
    for x in range(int(len(s)/2)):
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return len(s) == 0
