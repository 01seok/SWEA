T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    max_h = max(max(row) for row in mountain)
    start = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_h:
                start.append((i, j))

    visited = [[0] * N for _ in range(N)]
    max_length = 0


    def dfs(r, c, length, cut):
        global max_length
        if length > max_length:
            max_length = length

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if mountain[nr][nc] < mountain[r][c]:
                    visited[nr][nc] = 1
                    dfs(nr, nc, length + 1, cut)
                    visited[nr][nc] = 0

                elif mountain[nr][nc] - K < mountain[r][c] and cut == 1:
                    original_h = mountain[nr][nc]
                    visited[nr][nc] = 1
                    mountain[nr][nc] = mountain[r][c] - 1
                    dfs(nr, nc, length + 1, 0)
                    visited[nr][nc] = 0
                    mountain[nr][nc] = original_h


    for r0, c0 in start:
        visited[r0][c0] = 1
        dfs(r0, c0, 1, 1)
        visited[r0][c0] = 0
    print(f'#{tc} {max_length}')