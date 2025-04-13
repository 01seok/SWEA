T = int(input())

def enq(item):  # 최소 힙에 새로운 원소를 삽입하는 함수
    global last # 마지막 노드 위치 갱신을 위해 글로벌 선언
    last += 1   # 새 원소를 들어갈 last
    heap[last] = item   # 새 원소를 마지막 위치에 넣어주기
    
    c = last    # 새로 삽입한 자식노드
    p = c // 2  # 부모 노드는 자식 노드번호 // 2
    
    while p > 0 and heap[p] > heap[c]: # 부모 노드가 더 크면 자리 바꾸기
        heap[p], heap[c] = heap[c], heap[p]
        c = p   # 현재 노드를 부모 노드로 이동
        p = c // 2  # 부모 노드 업데이트
        
        
        
def deq():   # 최소 힙에서 루트 삭제하는 함수
    global last
    
    root = heap[1] # 루트 노드 저장
    heap[1] = heap[last]    # 제일 밑 마지막 노드를 루트로 올리기
    last -= 1   # last 노드 하나 줄이기
    
    p = 1   # 현재 루트
    c = p * 2   # 왼쪽 자식 노드
    
    while c <= last:    # 자식 노드가 존재하는 동안만 반복
        if c + 1 <= last and heap[c] > heap[c+1]:   # 오른쪽 자식 존재하고 왼쪽보다 값이 더 작다면 오른쪽을 선택
            c = c + 1 # 더 작은 자식 선택
            
        if heap[p] > heap[c]: # 부모가 자식보다 크다면 바꿔주기
            heap[p], heap[c] = heap[c], heap[p]
            p = c   # 부모 노드 갱신
            c = p * 2   # 새 부모의 왼쪽 자식
                
        else:   # 최소 힙 설정 끝나면 종료
            break
    return root # 원래 루트 노드 값 반환

for tc in range(1, T + 1):
    N = int(input())  # 노드 개수
    arr = list(map(int, input().split()))

    # 힙 초기화
    heap = [0] * (N + 1)  # 0번 인덱스 사용 안함
    last = 0  # 마지막 노드 위치 초기화

    # 입력 받은 값들 힙에 삽입
    for num in arr:
        enq(num)

    # 마지막 노드의 부모 노드 값 더해주기
    last_idx = last  # 마지막 노드 위치
    sum_result = 0  #  부모 노드들의 합

    while last_idx > 1:  # 루트는 제외
        last_idx = last_idx // 2  # 부모 노드로 이동
        sum_result += heap[last_idx]  # 부모 노드 값 추가


    print(f"#{tc} {sum_result}")