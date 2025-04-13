T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 돌 개수, 뒤집기 횟수
    stones = list(map(int, input().split())) # 흰색 0, 검정색 1
    
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1  # 1-based 인덱스를 0-based로 변환

        # j개의 돌을 양쪽으로 분배
        left_stones = j // 2
        right_stones = j // 2

        # 양쪽 범위 내에서 비교 후 뒤집기
        for k in range(1, left_stones + 1):
            left = i - k
            right = i + k
            if 0 <= left < N and 0 <= right < N:  # 범위를 벗어나지 않는 경우
                if stones[left] == stones[right]:  # 같은 색이면 뒤집기
                    stones[left] = 1 - stones[left]
                    stones[right] = 1 - stones[right]

    # 결과 출력
    print(f"#{tc} {' '.join(map(str, stones))}")