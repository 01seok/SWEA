T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())    # N개 상자, Q회
    boxes = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for idx in range(L-1, R):
            boxes[idx] = i


    print(f'#{tc}', *boxes)