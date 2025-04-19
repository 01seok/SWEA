import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra(N, graph):
    INF = int(21e8)
    dist = [[INF] * N for _ in range(N)]    # N * N 가중치 저장할 2차원 리스트
    dist[0][0] = 0  # 시작 지점에서 가중치는 0

    pq = [] # 우선순위 큐
    heapq.heappush(pq, (0, 0, 0))   # 누적 가중치, 행번호, 열번호 우선순위 큐에 넣어주기

    while pq:
        cost, r, c = heapq.heappop(pq)

        if (r, c) == (N-1, N-1):    # 끝지점에 도착하면
            return cost # 종료지점까지의 최소 누적 가중치 반환

        if cost > dist[r][c]:
            continue    # 더 최소의 경로가 있으면 pass

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                fuel_cost = graph[nr][nc] - graph[r][c]
                move_cost = 1 + max(0, fuel_cost)
                real_cost = cost + move_cost

                if real_cost < dist[nr][nc]:
                    dist[nr][nc] = real_cost
                    heapq.heappush(pq, (real_cost, nr, nc))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra(N, graph)
    print(f'#{tc} {result}')