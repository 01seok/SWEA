T = 10
N = 8
# M = 찾아야하는 회문의 길이
for tc in range(1, T+1):
 
    M = int(input())
    arr = [list(input()) for _ in range(N)]
 
    # 회문의 개수 (답)
    count = 0
 
    # 모든 위치에서 시작해서 길이가 M인 회문을 만들어보자
    # 행 i, 열 j
    # 모든 위치(i,j)에서 회문을 만들어본다. 길이 M 짜리
    # 가로 : (i,j) ~ (i, j + M) => 가로 문자열 하나 만들어서 회문인지 판단
    # 세로 : (i,j) ~ (i + M, j) => 세로 문자열 하나 만들어서 회문인지 판단
 
    # 행 우선 순회
    for i in range(N):
        for j in range(N-M+1): # 회문을 만들 수 있는 j 범위는 N - M + 1(인덱스라서) 혹은 if j + m < n
            s = arr[i][j: j + M] # 현재 회문을 만들어 볼 범위
            for k in range(len(s) // 2):
                if s[k] != s[len(s) - 1 - k]:
 
                    break  # 뒤에 볼 필요가 없어서
 
            else: # 반복문이 break를 통해서 중단 되지 않는다면 실행되는 부분
                count += 1
 
    for j in range(N):
        for i in range(N-M+1):
            s = [arr[i + k][j] for k in range(M)]
 
            for k in range(len(s) // 2):
                if s[k] != s[len(s) - 1 - k]:
 
                    break  # 뒤에 볼 필요가 없어서
 
            else: # 반복문이 break를 통해서 중단 되지 않는다면 실행되는 부분
                count += 1
 
    print(f'#{tc} {count}')