T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    if (N - 1) % 2 == 1:
        winner = 'Alice'
    else:
        winner = 'Bob'
    print(f'#{tc} {winner}')