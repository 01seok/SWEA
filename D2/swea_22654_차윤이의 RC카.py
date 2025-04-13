T = int(input())
dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]

for tc in range(1, T + 1):
    N = int(input())    # 필드 크기
    field = [list(input())  for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                start_r, start_c = r, c
            elif field[r][c] == 'Y':
                goal_r, goal_c = r, c

    Q = int(input())
    result = []
    for _ in range(Q):
        C, commands = input().split()
        C = int(C)
        commands = list(commands)

        r, c = start_r, start_c
        dir = 0

        for command in commands:
            if command == 'A':
                nr, nc = r + dr[dir], c + dc[dir]
                if 0 <= nr < N and 0 <= nc < N and field[nr][nc] != 'T':
                    r, c = nr, nc

            elif  command =='L':
                dir = (dir + 3) % 4
            elif command == 'R':
                dir = (dir + 1) % 4

        if (r, c) == (goal_r, goal_c):
            result.append(1)
        else:
            result.append(0)

    print(f'#{tc}', *result)