str = input()
cnt = 0
for i in str:
    if cnt == 10:
        print()
        cnt = 0
    print(i, end='')
    cnt += 1