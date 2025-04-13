def post_order(n):
    if node_sum[n]:
        return node_sum[n]

    left, right = 0, 0
    if 2 * n <= N:
        left = post_order(2 * n)
    if 2 * n + 1  <= N:
        right = post_order(2 * n + 1)
    node_sum[n] = left + right
    return node_sum[n]

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    node_sum = [0] * (N + 1)

    for _ in range(M):
        idx, val = map(int, input().split())
        node_sum[idx] = val

    result = post_order(L)

    print(f'{tc} {result}')