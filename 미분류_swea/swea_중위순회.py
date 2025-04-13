def in_order(n):
    if n:
        in_order(left[n])
        result.append(lst[n])
        in_order(right[n])


for tc in range(1, 11):
    N = int(input())    # 노드의 수
    lst = [''] * (N+1)      # 노드의 문자 저장할 곳
    left = [0] * (N+1)
    right = [0] * (N+1)
    result = []             # 중위 순회 결과 저장 리스트

    for _ in range(N):
        temp = input().split()  # N줄에 걸쳐 받는 입력 값들
        idx = int(temp[0])  # 첫번째 값은 현재 노드 번호
        lst[idx] = temp[1]  # 두번째 값은 현재 노드에 저장된 문자

        if len(temp) > 2:   # 세번째 요소 있으면 왼쪽 노드
            left[idx] = int(temp[2])

        if len(temp) > 3:   # 네번째 요소 있으면 오른쪽 노드 있음
            right[idx] = int(temp[3])

    in_order(1)
    print(f"#{tc} {''.join(result)}")