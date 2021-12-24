l = [1, 8, 11, 3]
a = 10
b = 1

def solve(l, a, i, memo = {}):
    if i >= len(l):
        return 0

    if i == len(l)-1:
        return l[i]

    if a > 0:
        c = 0
        _min = 100000
        while i < len(l)-1:
            c += l[i]
            _min = min(_min, max(c, solve(l, a-1, i+1, memo)))
            i += 1
    c = 0
    for j in range(i, len(l)):
        c += l[j]
    return c


print(solve(l, a-1, b, 0))