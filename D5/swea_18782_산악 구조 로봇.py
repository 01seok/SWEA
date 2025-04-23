from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(N, mountain, tunnel_list):
    visited = [[90000] * N for _ in range(N)]
    q = deque()
    visited[0][0] = 0
    q.append((0, 0, 0))
    while q:
        r, c, fuel = q.popleft()

        if fuel > visited[r][c]:
            continue

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0<=nr<N and 0<=nc<N:
                gap = mountain[nr][nc] - mountain[r][c]

                if gap > 0:
                    cost = gap * 2
                elif gap == 0:
                    cost = 1
                else:
                    cost = 0

                new_fuel = fuel + cost
                if new_fuel < visited[nr][nc]:
                    visited[nr][nc] = new_fuel
                    q.append((nr, nc, new_fuel))

        for tunnel in tunnel_list:
            r1, c1, r2, c2, t_cost = tunnel
            r1 -= 1
            c1 -=1
            r2 -=1
            c2 -=1

            if r == r1 and c == c1:
                if fuel + t_cost < visited[r2][c2]:
                    visited[r2][c2] = fuel + t_cost
                    q.append((r2, c2, fuel+t_cost))
            elif r == r2 and c == c2:
                if fuel + t_cost < visited[r1][c1]:
                    visited[r1][c1] = fuel + t_cost
                    q.append((r1, c1, fuel + t_cost))
    return visited[N-1][N-1]


T = int(input())
for tc in range(1, T +1):
    N, M = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    tunnel_list = [list(map(int, input().split())) for _ in range(M)]

    result = bfs(N, mountain, tunnel_list)
    print(f'#{tc} {result}')