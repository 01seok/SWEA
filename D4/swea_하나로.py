def find_set(x):
    if x == parents[x]:
        return x

    # 경로 압축 코드
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    tax = float(input())

    parents = [i for i in range(N)]
    min_cost = 0

    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            cost = (((x_lst[i] - x_lst[j]) ** 2) + ((y_lst[i] - y_lst[j]) ** 2)) * tax
            edges.append((cost, i, j))
    edges.sort()

    cnt = 0 # 간선의 개수를 세기 위해, n개 노드이므로 n-1개 간선이면 모든 노드 연결된 것
    for cost, i, j in edges:
        if find_set(i) != find_set(j):  # 섬끼리 연결되어있지 않다면
            union(i, j)
            min_cost += cost
            cnt += 1
        if cnt == N - 1:
            break

    print(f'#{tc} {min_cost:.0f}')