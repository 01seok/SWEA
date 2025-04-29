import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
INF = float("inf")
T = int(input())
for tc in range(1, T  + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    # 누적 가중치 저장해둘 dist
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0  # 첫 출발지에서는 가중치 0
    # heap에서 누적 가중치, r, c 담기
    heap = [(0, 0, 0)]

    while heap:
        time, r, c = heapq.heappop(heap)

        if (r, c) == (N-1, N-1):    # 도착했으면 끝
            break

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                next_time = time + board[nr][nc]
                # 기존에 알고 있던 다음 목적지에서의 최소 가중치보다 작으면 갱신
                if next_time < dist[nr][nc]:
                    dist[nr][nc] = next_time
                    heapq.heappush(heap, (next_time, nr, nc))
    print(f'#{tc} {dist[N-1][N-1]}')