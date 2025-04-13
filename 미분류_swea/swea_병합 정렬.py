def merge_sort(start, end): # start: 정렬 시작 idx, end: 정렬 종료 idx

    if start == end - 1:    # 종료 조건, 1개 남았을 때 (더이상 나눌 수 없을 때)
        # 길이가 1일때의 시작, 끝을 return
        return start, end
 
    # 절반씩 나누기 (나눌 수 있으면 계속 반으로 나누기)
    mid = (start + end) // 2
 
    # 왼쪽 정렬
    left_s, left_e = merge_sort(start, mid)
    # 오른쪽 정렬
    right_s, right_e = merge_sort(mid, end)
 
    # 병합하여 정렬하기 왼쪽과 오른쪽 중에서 작은거부터 꺼내서 큰 배열 만들기
    # 왼쪽부분, 오른쪽 부분 합친 후에 다시 범위 return
    merge(left_s, left_e, right_s, right_e)

    return start, end # 정렬 완료
 
 
def merge(left_s, left_e, right_s, right_e):
    global cnt
 
    # l : 왼쪽 부분에서 제일 작은 원소, r: 오른쪽 파트에서 제일 작은 원소
    l, r = left_s, right_s
 
    # 왼쪽 마지막 원소의 크기가 오른쪽 마지막 원소보다 크면
    if arr[left_e-1] > arr[right_e-1]:
        cnt += 1
 
    # 두 배열 합쳐서 길이 구하기, 오른쪽 끝 - 왼쪽 시작점
    N = right_e - left_s
    result = [0] * N
    idx = 0 # 정렬 후 놓을 원소 위치
 
    # 정렬 시작
    # 왼쪽과 오른쪽 부분 중에서 제일 작은거부터
    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            result[idx] = arr[l]    # 왼쪽 원소 한개 봤으니 그 다음 왼쪽 원소 보기 위해 + 1
            l += 1
            idx += 1
        else:
            result[idx] = arr[r]
            # 오른쪽이 작아서 오른쪽부분의 원소를 result에 추가
            r += 1
            idx += 1
 
    # 왼쪽이나 오른쪽에 원소가 남아있지 않은 경우
    # 왼쪽 원소 없고 오른쪽에만 있는경우
    # 오른쪽 부분 남은거 모두 result에 추가
    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1
 
    # 왼쪽에만 있고 오른쪽 원소 없을 때
    # 왼쪽 부분 남은거 모두 result에 추가
    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1
 
    # 정렬 결과를 원래 배열에 복사
    for i in range(N):
        arr[left_s + i] = result[i]
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 합칠때 왼쪽의 마지막 원소가 오른쪽의 마지막 원소보다 큰 경우의 수
    cnt = 0
    merge_sort(0,N)
    print(f"#{tc} {arr[N//2]} {cnt}")   