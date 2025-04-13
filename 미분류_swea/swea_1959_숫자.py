'''
1959.숫자
A가 더 긴지, B가 더 긴지 정해지지 않음
N이 더 긴 경우, 긴 쪽에서 기준 위치 생각해보기
짧은쪽 idx, j 긴쪽 i
길이구간은 0부터 N-M 까지 (마주보는 원소 길이구간)
마주 보는 수 곱의 합 s, 기준 위치 바뀌면 s 초기화




'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 숫자열 A의 길이, M은 숫자열 B의 길이
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    max_v = -200 # 문제 조건 고려, 답이 음수가 될 수 있다 생각하고 잘 생각하고 입력 보고 구간 정하기
    # if N > M: 에 대한 코드임 밑에 for 문은
    if N < M:
        N,M = M,N
        A,B = B,A
    for i in range(N-M+1): # 긴 배열에서 기준 위치 = i
        s = 0 # 기준 위치부터 마주보는 원소들의 곱의 합
        for j in range(M): # 짧은 배열에서 비교하는 위치
            s += A[i+j] * B[j] # 마주보는 자리 원소의 곱의 합, 캡쳐 참고
        if max_v < s:
                max_v = s
    print(f'#{tc} {max_v}')