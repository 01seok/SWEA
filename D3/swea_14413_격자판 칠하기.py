T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    flag = True

    def possible(start_color):
        for r in range(N):
            for c in range(M):
                if (r+c) % 2 == 0:
                    expected = start_color
                else:
                    if start_color == '#':
                        expected = '.'
                    else:
                        expected = '#'

                if board[r][c] == '?':
                    continue
                else:
                    if board[r][c] != expected:
                        return False
        return True

    if possible('#') or possible('.'):
        print(f'#{tc} possible')
    else:
        print(f'#{tc} impossible')