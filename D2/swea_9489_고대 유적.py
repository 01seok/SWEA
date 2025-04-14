T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N: 행 M: 열
    field = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0

    for r in range(N):
        length = 0
        for c in range(M):
            if field[r][c] == 1:
                length += 1

            else:
                max_len = max(max_len, length)
                length = 0

        max_len = max(max_len, length)

    for c in range(M):
        length = 0
        for r in range(N):
            if field[r][c] == 1:
                length += 1

            else:
                max_len = max(max_len, length)
                length = 0

        max_len = max(max_len, length)


    print(f'#{tc} {max_len}')