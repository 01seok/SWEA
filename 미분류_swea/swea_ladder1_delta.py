def find_start(ladder):
    n = 100  # 사다리 배열의 크기
    start = 0
    # 마지막 행에서 '2'의 위치를 반복문을 통해 찾기
    for j in range(n):
        if ladder[n-1][j] == 2:
            start = j
            break

    # 정적으로 방향별 좌표 변화량 정의
    # 위쪽 이동: 행 -1, 열 0
    di_1 = -1
    dj_1 = 0

    # 좌측 이동: 행 0, 열 -1
    di_2 = 0
    dj_2 = -1

    # 우측 이동: 행 0, 열 +1
    di_3 = 0
    dj_3 = 1

    # 시작 위치: 바닥의 '2'가 위치한 좌표
    row, col = n - 1, start

    while row > 0:
        # 좌측 이동 가능: 현재 위치의 왼쪽 칸이 1인 경우
        if col > 0 and ladder[row][col - 1] == 1:
            # 좌측으로 연속해서 이동
            while col > 0 and ladder[row][col - 1] == 1:
                col += dj_2  # dj_2는 -1이므로 왼쪽 이동
            row += di_1  # 위쪽으로 이동 (di_1은 -1)
        # 우측 이동 가능: 현재 위치의 오른쪽 칸이 1인 경우
        elif col < n - 1 and ladder[row][col + 1] == 1:
            # 우측으로 연속해서 이동
            while col < n - 1 and ladder[row][col + 1] == 1:
                col += dj_3  # dj_3는 1이므로 오른쪽 이동
            row += di_1  # 위쪽으로 이동
        else:
            # 좌우 이동이 없으면 단순히 위로 이동
            row += di_1

    # 최상단에 도달했을 때의 열 번호가 시작점 x좌표
    return col