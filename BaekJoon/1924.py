import sys
mon = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
m, d = map(int, sys.stdin.readline().split())
s = 0
for i in range(m-1) :
    s += mon[i]
i = (s+d) % 7
print(day[i])
