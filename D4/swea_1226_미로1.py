from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, 11):
    _ = input()
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    q = deque([(1, 1)]) # 덱에 시작점 넣어주기
    visited[1][1] = 1
    result = 0

    while q:
        cur_r, cur_c = q.popleft()

        for d in range(4):
            nr, nc = cur_r + dr[d], cur_c + dc[d]
            if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc] and maze[nr][nc] != 1:
                if maze[nr][nc] == 3:
                    result = 1
                    break
                visited[nr][nc] = 1
                q.append((nr, nc))
        if result:
            break
    print(f'#{tc} {result}')
