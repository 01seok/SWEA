# swea sum

'''

# 1. 입력받기

# 리스트 생성(max값 찾을)

# 2. 한 행씩 합 더하고 리스트에 담기

# 3. 전치

# 4. 한 행씩 합 더하고 리스트에 담기

# 5. (0,0) -> (99,99) 방향 대각선의 원소들 합 구하고 리스트에 담기

# 6. (0,99) -> (99,0) 방향 대각선의 원소들 합 구하고 리스트에 담기

# 7. 리스트에서 max로 최댓값 찾아서 결과 출력

'''





import sys
sys.stdin = open('input.txt', 'r') 
T = 10

for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = []
    for temp in arr:     # temp : 리스트 각 행들 (내부 리스트)
        result.append(sum(temp)) # 리스트 각 행들의 합
        
    arr_trans = list(zip(*arr)) # arr 행렬 전치
    for temp in arr_trans: 
        result.append(sum(temp)) # 전치 한 행들의 합
    
    left_diag = 0
    right_diag = 0 
       
    for i in range(100):
        for j in range(100):
            if i == j:
                left_diag += arr[i][j]
            if i + j == 99:
                right_diag += arr[i][j]
                
    result.append(left_diag)
    result.append(right_diag)
    
                
    print(f'#{tc} {max(result)}')                    