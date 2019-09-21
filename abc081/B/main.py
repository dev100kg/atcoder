num_length = int(input())
num_list = list(map(int, input().split()))
result_list = []

for num in num_list:
    result_list.append(int(format(num, 'b')[::-1].find('1')))
print(min(result_list))
