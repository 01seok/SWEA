'''
행의 숫자 M, 열의 숫자 N
풍선에 들어있는 꽃가루 갯수 A
'''

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    
    max_flower = 0 # 터진 꽃가루 개수
    
    for r in range(N):
        for c in range(M):
            cnt = A[r][c] # 터뜨린 풍선의 꽃가루 개수
   
            
            for d in range(4):
                
                    nr = r + dr[d] 
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M:
                        cnt += A[nr][nc]
                        
            max_flower = max(max_flower, cnt)
            
    print(f'#{tc} {max_flower}')