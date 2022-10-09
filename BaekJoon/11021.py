import sys
cnt = int(sys.stdin.readline())
for i in range(cnt) :
    n1, n2 = map(int, sys.stdin.readline().split())
    print('Case #{}: {}'.format(i+1, n1+n2))