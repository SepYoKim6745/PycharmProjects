import sys
while True:
    try:
        n1, n2 = map(int, sys.stdin.readline().split())
        print(n1+n2)
    except:
        break