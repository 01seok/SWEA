def dfs(col, cost):
    global min_cost
    
    if min_cost <= cost:    # 가지치기, 이미 구해둔 최소값보다 크다면 패스
        return

    if col == N:    # 모든 열 다 봤으면 최소값 갱신하고 종료
        min_cost = min(min_cost, cost)
        return
    
    for row in range(N):
        if used[row] == 1:
            continue
        
        used[row] = 1
        dfs(col + 1, cost + factory[row][col])
        used[row] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    
    used = [0] * N
    min_cost = float('inf')
    
    dfs(0, 0)
    print(f'#{tc} {min_cost}')