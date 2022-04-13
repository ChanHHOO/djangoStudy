a = int(input())
cnt = 0
for i in range(a, -1, -2):
    print((" "*cnt)+'*'*(i))
    cnt += 1
cnt = a//2
cnt -= 1
for i in range(1, a+1, 2):
    if i != 1:
        print((" "*cnt)+'*'*(i))
        cnt -= 1