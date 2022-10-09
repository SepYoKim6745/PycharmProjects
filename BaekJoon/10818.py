import sys
size = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
print(min(list), max(list))