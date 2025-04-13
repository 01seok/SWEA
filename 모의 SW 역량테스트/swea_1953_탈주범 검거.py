from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1

    while q:
        now_r, now_c = q.popleft()
        dir = types[graph[now_r][now_c]]

        for d in range(4):
            if dir[d] == 0:
                continue
            next_r, next_c = now_r + dr[d], now_c + dc[d]

            if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c] and graph[next_r][next_c] != 0:
                next_dir = types[graph[next_r][next_c]]

                if d % 2 == 0 and next_dir[d+1] == 0:
                    continue
                if d % 2 == 1 and next_dir[d-1] == 0:
                    continue

                if visited[now_r][now_c] + 1 > L:
                    continue
                visited[next_r][next_c] = visited[now_r][now_c] + 1
                q.append((next_r, next_c))


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)
    cnt = 0
    for r in range(N):
        for c in range(M):
            if 0 < visited[r][c] <= L:
                cnt += 1
    print(f'#{tc} {cnt}')