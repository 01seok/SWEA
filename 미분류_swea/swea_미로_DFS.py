T = int(input())

def dfs(sr, sc):
    stack = [(sr, sc)]
    visited = [[0] * N for _ in range(N)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while stack: # stack이 비게되면 종료
        r, c = stack.pop()
        visited[r][c] = 1 # 방명록 작성

        if maze[r][c] == 3:
            return 1
        # 3이 아니라면 델타 탐색 시작
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                stack.append((nr, nc))
                
    return 0

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    
    
    sr, sc = 0, 0
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c
    
    print(f'#{tc} {dfs(sr, sc)}')