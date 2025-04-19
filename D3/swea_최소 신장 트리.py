def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parents[root_y] = root_x

    else:
        parents[root_x] = root_y

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())    # 마지막 노드번호, 간선의 개수
    edges = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((w, s, e)) # 가중치 오름차순으로 정렬하기 위해

    edges.sort()
    parents = [i for i in range(V + 1)] # 0번부터 V번까지 노드 존재하니

    cnt = 0
    total_weight = 0

    for w, s, e in edges:
        if find_set(s) != find_set(e):
            union(s, e)
            total_weight += w
            cnt += 1
            if cnt == V:    # 모든 노드 연결 되었다면 (연결된 간선이 정점 수 -1개면)
                break   # 종료
    print(f'#{tc} {total_weight}')