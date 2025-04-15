T = int(input())
dr = [0, 1, 0, -1]  # 우 하 좌 상
dc = [1, 0, -1, 0]
for tc in range(1, T + 1):
    N = int(input())    # 달팽이 껍질 크기
    snail = [[0] * N for _ in range(N)]
    r, c, d = 0, 0, 0
    num = 1

    while num <= N ** 2:
        snail[r][c] = num
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
            r, c = nr, nc
        else:
            d = (d+1) % 4
            r += dr[d]
            c += dc[d]
        num += 1


    print(f'#{tc}')
    for row in snail:
        print(*row)