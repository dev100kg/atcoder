n = int(input())
mochi_list = []
for i in range(0, n):
    mochi_list.append(int(input()))
print(len(list(set(mochi_list))))
