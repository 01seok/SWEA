'''
250416 gpt 사용해서 구현 도움 받아서 푼 문제
'''


from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(N, M, field):
    # 바이러스 몇 초에 퍼졌지 체크 할 visited
    virus_visited = [[-1] * M for _ in range(N)]
    # 삼성 몇초에 방문했는지 체크 할 visited
    visited = [[-1] * M for _ in range(N)]

    # 바이러스 큐
    virus_q = deque()
    # 삼성 큐
    samsung_q = deque()

    for r in range(N):
        for c in range(M):
            if field[r][c] == 2:
                # 바이러스 시작 위치
                virus_q.append((r, c, 0))
                virus_visited[r][c] = 0
            elif field[r][c] == 3:
                # 삼성 시작 위치
                samsung_q.append((r, c, 0))
                visited[r][c] = 0

    # 바이러스 퍼지는 시뮬레이션 시작
    while virus_q:
        r, c, t = virus_q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 바이러스가 아직 안 간 곳이고 벽이 아닌 곳이면 바이러스 퍼질 수 있음
            if 0 <= nr < N and 0 <= nc < M:
                if field[nr][nc] != 1 and virus_visited[nr][nc] == -1:
                    virus_visited[nr][nc] = t + 1
                    virus_q.append((nr, nc, t + 1))

    # 바이러스 어떻게 퍼질지 알았으니 삼성 이동 시작하며 결과 구하기
    while samsung_q:
        r, c, t = samsung_q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 맵 밖에 있으면 탈출 성공한거
            if not (0 <= nr < N and 0 <= nc < M):
                return t + 1  # 탈출에 걸린 시간

            # 이동 불가 조건
            if field[nr][nc] == 1:    # 벽이면 못감
                continue
            if visited[nr][nc] != -1:   # 이미 방문한 칸이면 생략
                continue
            if virus_visited[nr][nc] != -1 and virus_visited[nr][nc] <= t + 1:
                # 바이러스가 그 칸에 t+1초보다 먼저 또는 동시에 도달했으면 못 감
                continue

            # 이동 가능
            visited[nr][nc] = t + 1
            samsung_q.append((nr, nc, t + 1))

    # 탈출 불가거나 좀비인 경우 구별하기
    flag = False
    for r in range(N):
        for c in range(M):
            if visited[r][c] != -1: # 이미 가본 곳이고
                if virus_visited[r][c] == -1:   # 바이러스도 못 가본 곳이면
                    flag = True
                    break   # 이 경우는 더 볼 것 없고
        if flag:
            break   #이 열을 다 돌아도 감염 안됐다면 볼 거 없고
    if flag:
        return "CANNOT ESCAPE"  # 모든 행, 열 다 돌았는데도 감염 안된거니
    else:
        return "ZOMBIE"


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 세로 N, 가로 M
    field = [list(map(int, input().split())) for _ in range(N)]
    result = bfs(N, M, field)
    print(f'#{tc} {result}')