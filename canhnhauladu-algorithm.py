def findSmallestString(s):
    result = ""
    stack = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            stack += 1
        elif stack > 1:
            if s[i] < s[i+1]:
                result += s[i]*stack
            stack = 1
        else:
            if s[i] < s[i+1]:
                result += s[i]
        result += s[i]
    result += s[-1]
    return result

n = int(input())
for i in range(n):
    s = input()
    print(f"Case #{i+1}: {findSmallestString(s)}")
