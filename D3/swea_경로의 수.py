def dfs(node):
    global cnt
    if node == G:   # 목표 노드 도착하면 경로 1 추가 후 종료
        cnt += 1
        return

    for next_node in adj[node]:
        if visited[next_node]:  # 이미 갔던 곳이면 패스
            continue
        visited[next_node] = 1  # 다음 노드 방문처리하고
        dfs(next_node)          # 다음 노드 재귀 호출
        visited[next_node] = 0  # 다음 탐색을 위해 방문 표시 초기화

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())    # N: 마지막 정점 번호, E: 간선 개수
    edges = list(map(int, input().split()))  # 간선 정보, 2 * E개 정수 입력

    adj = [[] for _ in range(N+1)]  # 인접 리스트 생성
    for i in range(0, len(edges), 2):   #  출발, 도착이니 2개씩 묶어보기
        start, end = edges[i], edges[i + 1]
        adj[start].append(end)  # 출발 노드 -> 도착 노드 방향성 간선 인접 리스트에 입력

    S, G = map(int, input().split())    # 시작점, 목표점

    visited = [0] * (N+1)
    cnt = 0 # 경로 개수 저장 변수
    visited[S] = 1  # 시작 정점 방문 처리하고 dfs 시작
    dfs(S)

    print(f'#{tc} {cnt}')