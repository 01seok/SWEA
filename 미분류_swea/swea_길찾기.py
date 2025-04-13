# 총 10개의 테스트 케이스가 주어진다고 가정합니다.
for _ in range(10):
    # 첫 줄에는 테스트 케이스 번호와 전체 간선(길)의 개수가 공백으로 구분되어 주어진다.
    # 예: "1 16" → 테스트 케이스 번호는 "1", 간선의 개수는 16개
    line = input().split()      # 입력 받은 문자열을 공백으로 분리
    tc = line[0]                # 테스트 케이스 번호 (문자열)
    edge_count = int(line[1])   # 간선(길)의 총 개수를 정수로 변환

    # 두 번째 줄에는 간선 정보가 하나의 숫자 나열로 주어진다.
    # 이 숫자들은 순서대로 두 개씩 묶여서 (u, v) 형태의 간선을 나타냅니다.
    edge_data = list(map(int, input().split()))

    # 정점(도시)의 개수는 100개(0번부터 99번)로 고정되어 있다.
    # 각 정점에서 출발하는 간선 정보를 저장할 리스트를 100개 생성합니다.
    graph = [[] for _ in range(100)]
    
    # edge_data에서 2개씩 읽어 (u, v) 간선을 그래프에 추가합니다.
    for i in range(0, len(edge_data), 2):
        u = edge_data[i]       # 간선의 시작점
        v = edge_data[i + 1]   # 간선의 도착점
        graph[u].append(v)     # u에서 갈 수 있는 도시 리스트에 v 추가 (일방통행)

    # 방문 여부를 저장할 리스트 (0번부터 99번 도시까지)
    visited = [False] * 100

    # DFS(깊이 우선 탐색) 재귀 함수 정의
    def dfs(node):
        # 만약 현재 노드가 도착점 99라면, 경로가 존재하는 것이므로 True 반환
        if node == 99:
            return True
        
        # 현재 노드를 방문 처리
        visited[node] = True
        
        # 현재 노드에서 갈 수 있는 모든 인접 노드(도시)에 대해 탐색
        for neighbor in graph[node]:
            # 아직 방문하지 않은 도시인 경우
            if not visited[neighbor]:
                # neighbor를 시작점으로 DFS 재귀 호출
                if dfs(neighbor):
                    # 만약 재귀 호출을 통해 99번 도시에 도달했다면, 바로 True 반환
                    return True
        # 모든 경로를 탐색했으나 99번 도시에 도달하지 못하면 False 반환
        return False

    # DFS를 0번 도시에서 시작하여 경로 존재 여부를 확인
    result = dfs(0)

    # 결과 출력: 테스트 케이스 번호 앞에 '#'를 붙이고, 경로가 존재하면 1, 없으면 0 출력
    print(f"#{tc} {1 if result else 0}")