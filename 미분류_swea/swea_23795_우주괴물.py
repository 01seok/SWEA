T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for r in range(N):
        for c in range(N):
            if arr[r][c] ==2:
                for d in range(4):
                    for k in range(1, N):
                        nr = r + dr[d] * k
                        nc = c + dc[d] * k
                        
                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            break
                        if arr[nr][nc] in (1, 2):
                            break
                        
                        arr[nr][nc] = 3
                    
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                cnt += 1
                
    print(f'#{tc} {cnt}')                    
            