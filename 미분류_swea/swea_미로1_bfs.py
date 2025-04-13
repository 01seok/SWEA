T = 10
N = 16

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    input()
    
    maze = [list(map(int, input())) for _ in range(N)] # 미로 입력
    
    r, c = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j # 출발점 2 찾음
                
    from collections import deque

    visited = [[0] * N for _ in range(N)] # 방명록 만들기
    q = deque()

    q.append((r, c)) # 현재 위치 및 갈 수 있는 곳 들 큐에 추가
    visited[r][c] = True # 다음 노드 도착하면 방명록 작성 바로

    ans = 0 # 길이 있는지 없는지 ?

    while q:
        now_r, now_c = q.popleft() # 큐에 저장되어 있는 갈 수 있는 곳들 탐색 (앞에서 부터 빼내보자)
        
        if maze[now_r][now_c] == 3: # 탐색 했더니 목적지 3이 있다?
            ans = 1 # 길 있음
            break # 그만 탐색
        
        # 그게 아니라면 델타 탐색하며 길을 찾아라
        for d in range(4):
            nr = now_r + dr[d]
            nc = now_c + dc[d]
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] != 1:
                # 배열 범위를 벗어나지 않고 방문하지 않았어야하며, 1(벽)이 아닌 곳들만 갈 수 있음
                visited[nr][nc] = True    # 방문한 곳 방명록 작성
                q.append((nr, nc)) # 큐에 방문한 곳 넣기
            
    print(f'#{tc} {ans}')