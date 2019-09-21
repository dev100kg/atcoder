n, a, b = list(map(int, input().split()))
ans = 0
for i in range(0, n+1):
    tmp = 0
    for j in range(0, len(str(i))):
        tmp += int(str(i)[j])
    if tmp >= a and tmp <= b:
        ans += i
print(ans)
