input()
card_list = sorted(list(map(int, input().split())), reverse=True)
print(sum(card_list[::2]) - sum(card_list[1::2]))
