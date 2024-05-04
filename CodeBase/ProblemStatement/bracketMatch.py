def bracketmatch(str1):
    bal = 0
    ans = 0
    for i in range(0, len(str1)):
        if str1[i] == '(':
            bal += 1
        else:
            bal += -1
        # It is guaranteed bal >= -1
        if bal == -1:
            ans += 1
            bal += 1
    return bal + ans

print(bracketmatch('))(('))