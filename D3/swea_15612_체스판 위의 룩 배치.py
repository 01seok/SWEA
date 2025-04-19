T = int(input())
for tc in range(1, T + 1):
    board = [list(input()) for _ in range(8)]

    flag = True
    for r in range(8):
        cnt = 0
        for c in range(8):
            if board[r][c] == 'O':
                cnt += 1
        if cnt != 1:
            flag = False
            break


    for c in range(8):
        cnt = 0
        for r in range(8):
            if board[r][c] == 'O':
                cnt += 1

        if cnt != 1:
            flag = False
            break

    if flag:
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')