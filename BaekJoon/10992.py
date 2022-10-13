import sys

n = int(sys.stdin.readline())
for i in range(1, n + 1):
    if i == 1:
        print(' ' * (n - i) + '*')
    elif i == n:
        print('*' * (n * 2 - 1))
    else:
        print(' ' * (n - i) + '*' + ' ' * (i * 2 - 3) + '*')
