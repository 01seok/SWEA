T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    count = 0  # 스위치 조작 횟수
    switch_count = 0    # 지금까지 몇 번 반전(스위치 조작)이 있었는지
    
    for i in range(N):
        # 지금까지의 반전 횟수(flip_count)의 패리티에 따라 전등의 실제 상태를 결정
        if switch_count % 2 == 0:
            # 반전 횟수가 짝수이면 전등 상태는 A[i]와 동일
            light_status = A[i]
        else:
            # 반전 횟수가 홀수이면 전등 상태는 반전되어 1 - A[i]가 됨
            light_status = 1 - A[i]
            
        # 현재 전등들의 상태와 목표 상태(B[i])가 다르면, i번 스위치를 눌러 상태를 맞춰줘야 함
        if light_status != B[i]:
            count += 1   # 스위치 조작 횟수를 증가
            switch_count += 1     # 전체 반전 횟수도 증가시킴
    
    print(f"#{tc} {count}")