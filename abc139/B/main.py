a, b = map(int, input().split())
total_socket = 0
socket_count = 0
while total_socket < b:
    if socket_count >= 1:
        total_socket += (a-1)
    else:
        total_socket += a
    socket_count += 1
print(socket_count)
