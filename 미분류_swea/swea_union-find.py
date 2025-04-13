# 경로 압축을 적용한 find 함수
def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

# 랭크를 이용한 union 함수
def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return  # 이미 같은 집합이면 합칠 필요 없음
    # 랭크를 비교하여 더 큰 쪽을 대표로 결정
    if rank[rx] > rank[ry]:
        p[ry] = rx
    else:
        p[rx] = ry
        if rank[rx] == rank[ry]:
            rank[ry] += 1

T = int(input())
for tc in range(1, T + 1):
    # N: 전체 원소의 수, M: 같은 그룹이어야 하는 관계의 수
    N, M = map(int, input().split())
    
    # 처음엔 각각 자기 자신이 대표가 되도록 설정
    p = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    
    # M개 관계에 대해 union 함수
    for _ in range(M):
        data = list(map(int, input().split()))
        for i in range(0, len(data), 2):
            a, b = data[i], data[i+1]
            union(a, b)

    # 중복되지 않는 대표의 수 = 그룹 개수
    groups = set()
    for i in range(1, N + 1):
        groups.add(find_set(i))

    print(f'#{tc} {len(groups)}')