for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    row = 99
    col=  ladder[row].index(2)

    while row > 0:
        if col > 0 and ladder[row][col-1] == 1:
            while col >0 and ladder[row][col-1] == 1:
                col -= 1
        elif col < 99 and ladder[row][col+1] == 1:
            while col <99 and ladder[row][col+1] == 1:
                col += 1

        row -= 1

    print(f'#{tc} {col}')