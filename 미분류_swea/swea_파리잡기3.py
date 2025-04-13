 # 가로 세로 길이가 같은지 확인
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 배열의 크기
    # M : 스프레이 세기

    arr = [list(map(int, input().split())) for _ in range(N)] # 리스프 컴프리헨션


    # 최대로 잡을 수 있는 파리 수
    max_fly = 0

    # 상하좌우 델타 탐색 1번
    di_1 = [-1, 1, 0, 0]
    dj_1 = [0, 0, -1, 1]


    # 대각선 4방향 델타 탐색 2번
    di_2 = [-1, -1, 1, 1]
    dj_2 = [1, -1, -1, 1]

    for i in range(N):
        for j in range(N):
            
            center = arr[i][j] # 중심 값의 파리 수레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다. 스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
            total_plus = center # + 노즐 파리 수
            
            for k in range(1, M): # 스프레이 세기만큼 각 방향으로 k 칸
                for d in range(4): # 4방향, 인덱스로 접근해서 방향 별로 구하기
                    ni = i + di_1[d] * k
                    nj = j + dj_1[d] * k
                    
                    if 0 <= ni < N and 0 <= nj < N: # 배열 내에서 더하도록 설정
                        total_plus += arr[ni][nj] # + 노즐 파리 값
                        
            total_x = center # x 노즐 파리 수
            for k in range(1, M):
                for d in range(4):
                    ni = i + di_2[d] * k
                    nj = j + dj_2[d] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        total_x += arr[ni][nj]
            max_fly = max(max_fly, total_plus, total_x)
    # 그 중에 최댓값 구해서 출력
    print(f'#{tc} {max_fly}')