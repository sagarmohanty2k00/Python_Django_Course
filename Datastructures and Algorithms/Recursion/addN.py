n = int(input())

# with loop
sum = 0
for i in range(n+1):
    sum += i
    # 0, 1, 3, 6, 10, 15
    # sum(101) = sum(100) + 101
print(sum)

# with recursion
def sum(n):
    # base case
    if (n == 0):
        return 0

    sumN = sum(n-1) + n
    return sumN

print(sum(n))