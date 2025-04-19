from collections import deque

T = int(input())

# num : 입력 받는 시작 숫자
def bfs(num):
    q = deque() # bfs 탐색에 사용할 큐
    v = set()   # 탐색했던 숫자 보관할 visited set
    v.add(num)  # 연산 시작하는 숫자부터 넣고 시작
    q.append((num, 0))  # 큐에 시작 숫자와 연산 횟수 넣어주기

    while q:    # 큐가 빌 때 까지 시작
        target, cnt = q.popleft()

        if target == M: # 꺼낸 숫자가 목표한 값이면 종료
            return cnt

        # next_num은 연산결과
        for next_num in (target+1, target-1, target * 2, target - 10):
            # 범위 체크, 중복 연산 아닌 경우에만
            if 1 <= next_num <= 1000000 and next_num not in v:
                v.add(next_num) # 탐색했다고 기록해주고
                q.append((next_num, cnt + 1))   # 다음 연산 위해 숫자와 연산 횟수 추가
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    min_cnt = bfs(N)
    print(f'#{tc} {min_cnt}')