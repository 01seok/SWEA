def postorder(t):   # 후위순회 함수
    # 숫자라면 그대로 반환 (리프노드라면)
    if c_left[t] == 0 and c_right[t] == 0:
        return values[t]  

    # 왼쪽 탐색 
    left_value = postorder(c_left[t])
    # 오른쪽 탐색
    right_value = postorder(c_right[t])

    # 현재 노드가 연산자인 경우 연산 진행
    if values[t] == '+':
        return left_value + right_value
    elif values[t] == '-':
        return left_value - right_value
    elif values[t] == '*':
        return left_value * right_value
    elif values[t] == '/':
        return left_value / right_value


for tc in range(1, 11):
    N = int(input())  # 정점 개수

    # 트리 구조 저장 공간 초기화
    values = [None] * (N + 1)  # 노드의 연산자 또는 숫자를 저장하는 리스트
    c_left = [0] * (N + 1)  # 각 노드의 노드 번호 저장
    c_right = [0] * (N + 1) 

    # 트리 데이터 입력받기
    for _ in range(N):
        data = input().split()  # 노드 데이터 입력받기 (숫자거나 연산자거나)
        idx = int(data[0])  # 입력조건에서 첫번째가 노드 번호임, 노드 번호

        if data[1].isdigit():  # 숫자인 경우
            values[idx] = int(data[1])  # int 형태로 values 리스트에 저장
        else:  # 연산자인 경우
            values[idx] = data[1]  # 연산자 values 리스트에 저장
            c_left[idx] = int(data[2])  # 왼쪽 자식 번호 저장
            c_right[idx] = int(data[3])  # 오른쪽 자식 번호 저장

    # 루트 노드인 1번 노드부터 후위 순회하여 연산
    result = postorder(1)

    print(f'#{tc} {int(result)}')