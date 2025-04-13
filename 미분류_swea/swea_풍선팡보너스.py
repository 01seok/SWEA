T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 사이즈
    balloon = [] # N x N 풍선들

    for _ in range(N):
        row = list(map(int, input().split()))
        balloon.append(row) # 가로(행)을 balloon에 추가해줌

    row_sum = [] # 각 행의 합을 저장할 리스트
    for i in range(N):
        s = 0  # i번째 행의 합 변수
        for j in range(N):
            s += balloon[i][j]  # i번째 행의 모든 숫자를 더함
        row_sum.append(s)

    col_sum = [] # 각 열의 합 저장할 리스트
    for j in range(N):
        s = 0  # j번째 열의 합을 저장
        for i in range(N):
            s += balloon[i][j]  # j번째 열의 모든 숫자를 더함
        col_sum.append(s)

    scores = [row_sum[i] + col_sum[j] - balloon[i][j] for i in range(N) for j in range(N)]
    bonus_score = max(scores) - min(scores)
    
    # boom_score = [] # 모든 위치에서 풍선 터트렸을 때 얻는 점수 저장할 리스트
    # for i in range(N):
    #     for j in range(N):
        
    #         # (i, j) 터트렸을 때 행의 합 + 열의 합 - (중복으로 센 해당 풍선의 숫자)
    #         score = row_sum[i] + col_sum[j] - balloon[i][j]
    #         boom_score.append(score)  # 계산된 점수를 boom_score에 추가

    # bonus_score = max(boom_score) - min(boom_score)
    
    print(f"#{tc} {bonus_score}")
    
