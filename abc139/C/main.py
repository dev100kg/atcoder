n = int(input())
list_h = list(map(int, input().split()))[::-1]
count = 0

for i in range(n):
    if list_h[i] <= list_h[i+1]:
        count += 1
print(count)
