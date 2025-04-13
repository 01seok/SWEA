T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 돌 개수, 뒤집는 횟수
    stones = list(map(int, input().split())) # 초기 상태 0 = 흰색, 1 = 검정색
    
    for _ in range(M):
        i, j = map(int, input().split()) # 뒤집는 시작 위치 i, 개수 j
        i -= 1 # 인덱스이므로 1 빼줘야함
        
        if i + j > N: # 리스트 범위를 초과하면 N을 끝으로 제한
            end = N
        else:
            end = i+j
            
        color = stones[i] # i번째 돌의 색이 기준
        for c in range(i, end):
            stones[c] = color # i번째 돌의 색으로 변경
            
    print(f"{tc} {' '.join(map(str, stones))}")