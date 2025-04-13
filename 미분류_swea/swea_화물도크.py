T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 작업 시간 리스트 시작시간과 끝 시간
    # s1 : 첫번째 작업의 시작시간
    # e1 : 첫번째 작업의 종료시간
    work_list = [list(map(int, input().split())) for _ in range(N)]

    # 정렬 기준을 index 1기준으로 sort하기 위해서 ! (람다 대신)
    def key_f(e):
        # 정렬 기준을 return
        return e[1]

    # 작업시간이 빠른 것이 앞으로 오게 정렬
    work_list.sort(key=key_f)

    # 이전 작업의 끝난 시간
    p_work_end = 0

    # 최대 작업 개수
    cnt = 0

    while work_list:
        # 이 현재 작업의 시작 시간이
        # 이전 작업의 끝 시간보다 뒤에 있어야 한다.
        work = work_list.pop(0)
        if work[0] >= p_work_end:
            cnt += 1
            # 작업 끝난 시간 갱신
            p_work_end = work[1]

    print(f"#{tc} {cnt}")
