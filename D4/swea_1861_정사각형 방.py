T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N +1)
    for r in range(N):
        for c in range(N):
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0<= nr < N and 0<= nc < N:
                    if field[nr][nc] == field[r][c] + 1:
                        visited[field[r][c]] = 1
                        break

    total, cnt, start = 0, 0, 0
    for i in range(1, N*N + 1):
        if visited[i] == 1:
            cnt += 1
        else:
            if total < cnt:
                total = cnt
                start = i - cnt
            cnt = 0
    print(f'#{tc} {start} {total+1}')