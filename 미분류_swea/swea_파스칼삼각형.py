# 왼쪽과 오른쪽 숫자의 합을 구하는 재귀함수
def lr_sum(arr):
    # 인자 arr = 이전 행의 숫자들
    # 종료 조건 : 리스트의 길이 1 이하이면 더 이상 계산할 인접 원소가 없으므로 빈 리스트 반환
    if len(arr) <= 1:
        return []
    # 현재 원소와 바로 오른쪽 원소의 합을 계산하고, 나머지에 대해 재귀 호출한 결과를 합쳐서 반환
    return [arr[0] + arr[1]] + lr_sum(arr[1:])

# 파스칼 삼각형을 생성하는 재귀함수
def pascal(n, arr=None):
    # arr은 현재 행이고 첫 호출에 값이 없으므로 [1]을 만들어줌
    if not arr:
        arr = [1]
    
    # 종료 조건: 현재 행의 길이가 n보다 커지면 더 이상 재귀 호출하지 않음
    if len(arr) > n:
        return
    
    # 첫 행인 경우 (arr의 길이가 1이면)
    if len(arr) == 1:
        print(*arr)
        # 다음 행은 [1, 1]이 되어야 하므로, arr+[1]을 전달하면서 재귀 호출
        return pascal(n, arr + [1])
    
    # [1] 이후의 행일 경우 현재 행을 출력
    print(*arr)
    
    # 다음 행은 양 끝은 1 고정이고, 가운데 숫자들은 lr_sum을 통해 계산
    arr = [1] + lr_sum(arr) + [1]
    
    # 새로 생성된 행을 가지고 재귀 호출하여 다음 행들을 출력
    return pascal(n, arr)


T = int(input())

for tc in range(1, T+1):
    # n = 삼각형 크기
    n = int(input())
    

    print(f'#{tc}')
    
    # 함수 내부에서 이미 print 수행
    pascal(n)