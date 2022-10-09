import sys
n = int(sys.stdin.readline())
for i in range(1,n):
    print('*'* i, ' '*((n-i)*2-2), '*'* i)
for j in range(n+1, 1) :
    print('*'*i)