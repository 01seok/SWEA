dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, length, path):
    if length == 7:
        numbers.add(path)
        return

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, length +1, path + board[nr][nc])

T = int(input())
for tc in range(1, T + 1):
    board = [input().split() for _ in range(4)]
    numbers = set()

    for r in range(4):
        for c in range(4):
            dfs(r, c, 1, board[r][c])
    print(f'#{tc} {len(numbers)}')