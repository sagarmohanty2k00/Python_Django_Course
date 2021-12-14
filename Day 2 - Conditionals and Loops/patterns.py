n = int(input())

# pattern 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# ...
print("Pattern - 1")
for row in range(n):
    for value in range(1, row+2):
        print(value, end=' ')
    print()

# pattern - 2
# 0 - 1              => 1+0
# 1 - 2 3            ...
# 2 - 4 5 6          => 1+3 2+3 3+3 => 6
# 3 - 7 8 9 10       => 6+1 6+2 6+3 6+4 => 10
# 4 - 11 12 13 14 15 => 10+1 10+2 10+3 10+4 10+5 => 15
# ...
print("Pattern - 2")
prevEnd = 0
for row in range(n):
    for increament in range(1, row+2):
        print(prevEnd+increament, end=' ')
    prevEnd += row + 1
    print()

# pattern - 3
#         1 - 0
#       1 2 - 1
#     1 2 3 - 2
#   1 2 3 4 - 3
# 1 2 3 4 5 - 4
# ...
print("Pattern - 3")
for row in range(n):
    # for i in range((n - (row+1) ) * 2):
    #     print(" ", end='')

    print(" "*(n - (row+1)) * 2, end='')
    
    for value in range(1, row+2):
        print(value, end=' ')
    print()




# pattern - 4
#     ***    ***     => 2s + [(4*n + n-1) - 8s ]/ 2 + 4s + [(4*n + n-1) - 8s ]/ 2 + 2s
#    *****  *****    => 1s + [(4*n + n-1) - 4s ]/ 2 + 2s + [(4*n + n-1) - 4s ]/ 2 + 1s
#   **************   => 4*n + n-1
#     **********     => 2s + 4*n + n-1 - 4s + 2s
#       ******       => 4s + 4*n + n-1 - 8s + 4s
#         **         => 6s + 4*n + n-1 - 12s + 6s
print("Pattern - 4 (Heart)")
for row in range(n-1):
    print(" "*(n-row-1), end='')
    print("*"*(((4*n + n-1) - (n-row-1)*4)//2), end='')
    print(" "*(n-row-1)*2, end='')
    print("*"*(((4*n + n-1) - (n-row-1)*4)//2), end='')
    print(" "*(n-row-1), end='')

    print()

print("*"*(4*n + n-1))

for row in range(n):
    print(" "*(row+1)*2, end='')
    print("*"*((4*n + n-1)-(row+1)*4), end='')
    print(" "*(row+1)*2, end='')

    print()