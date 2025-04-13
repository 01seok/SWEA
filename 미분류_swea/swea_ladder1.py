for tc in range(1, 11):

    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 가장 아래 행부터 시작
    row = 99
    # 2의 위치를 찾아 해당 열의 idx 저장
    col = ladder[row].index(2)  # 동작 구조 같은걸 정확히 파악하고 쓰기
    # x.y = 헷갈릴 수 있으니 r,c or i, j 써보기
    
    
    # 2에서 위로 거슬러 올라가면서 출발점 찾기
    # 0번째 행에 도착하면 탐색 종료
    while row > 0:
        # 현재 가장 왼쪽(idx 0)이 아니고 열의 왼쪽에 1이 있다면
        if col > 0 and ladder[row][col - 1] == 1:
            # 왼쪽에 1이 연속으로 있으면 왼쪽으로 계속 이동
            while col > 0 and ladder[row][col - 1] == 1:
                col -= 1  # 왼쪽으로 한 칸 이동
        # 현재 가장 오른쪽(idx 99)이 아니고, 왼쪽으로 더 이상 못가고 오른쪽에 1이 있을 때
        elif col < 99 and ladder[row][col + 1] == 1:
            # 오른쪽에 1이 연속으로 있으면, 오른쪽으로 계속 이동
            while col < 99 and ladder[row][col + 1] == 1:
                col += 1  # 오른쪽으로 한 칸 이동
        # 좌우 이동 while문이 끝나면 한 행 위로 올라감
        row -= 1  # 위로 한 칸 이동
    
    # 전체 while문 끝나면 col(출발점) 출력

    print(f"#{tc} {col}")
    
    