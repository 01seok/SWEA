T = int(input())
for tc in range(1, T + 1):
    N, K = map (int, input().split())   # 퍼즐 크기, 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result =0
    for r in range(N):
        cnt = 0
        for c in range(N):
            if puzzle[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    for c in range(N):
        cnt = 0
        for r in range(N):
            if puzzle[r][c] ==1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    print(f'#{tc} {result}')