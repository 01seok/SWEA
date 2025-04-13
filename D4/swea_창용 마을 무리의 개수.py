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
    # 랭크(집합의 높이)를 비교하여 더 큰 쪽을 대표로 결정
    if rank[rx] > rank[ry]:
        p[ry] = rx
    else:
        p[rx] = ry
        if rank[rx] == rank[ry]:
            rank[ry] += 1

T = int(input())
for tc in range(1, T + 1):
    #  N: 사람 수, M: 관계 수
    N, M = map(int, input().split())

    # 처음엔 자기자신을 대표로 설정
    p = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    # 중복되는 숫자 빼고 숫자가 무리(대표) 수 구하기
    groups = set()
    for i in range(1, N + 1):
        groups.add(find_set(i))

    print(f'#{tc} {len(groups)}')