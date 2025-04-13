def dfs(num, multiply):
    global max_per
    
    if max_per >= multiply:  # 이미 전에 구해둔 확률보다 같거나 낮으면 볼 필요 없음
        return  # 가지치기
    
    if num == N:    # 모든 직원 확률 다 구했으면
        max_per = max(max_per, multiply)  # 최대 확률 갱신 후 종료
        return
    
    for i in range(N):
        if used[i] == 1:    # 다른 직원이 이미 골랐으면
            continue        # 패스
        
        used[i] = 1 # 이 일 골랐다고 체크하고
        dfs(num + 1, multiply * (suc_per[num][i] / 100))
        # 그 직원 확률(인덱스num) 구해서 다른 일 한 직원들 확률과 곱해주며 재귀 호출
        used[i] = 0 # 다음 재귀 때 또 써야하니 0으로 초기화






T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    suc_per = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0  # 정답이 될 값, max_per에 100 곱해 줄 예정
    used = [0] * N  # 다른 직원이 고른 일인지 체크용
    max_per = 0 # 최대 확률
    
    dfs(0, 1)
    result = max_per * 100
    print(f'#{tc} {result:.6f}')
    