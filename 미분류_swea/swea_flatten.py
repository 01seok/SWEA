T = 10
for tc in range(1, T+1):
    dumps = int(input())
    boxes = list(map(int, input().split()))
 
    for _ in range(dumps):
        max_height = boxes[0] # 최댓값 박스 idx 첫번째로 설정
        max_idx = 0
        min_height = boxes[0] # 최솟값 박스 idx 첫번째로 설정
        min_idx = 0
        w = len(boxes) # 가로 길이 (반복문이 돌아갈 범위)
 
    # 반복문을 통해 모든 상자를 확인하고 더 높은 값 나오면 최댓값 갱신, 더 낮은 값 나오면 최솟값 갱신
 
        for i in range(w):
            if boxes[i] > max_height:
                max_idx = i
                max_height = boxes[i]
            if boxes[i] < min_height:
                min_idx = i
                min_height = boxes[i]
 
        boxes[max_idx] -= 1 # 최댓값 박스에서 1개씩 -
        boxes[min_idx] += 1 # 최솟값 박스에 1개씩 +
 
        max_height = max(boxes) # 박스 최댓값
        min_height = min(boxes) # 박스 최솟값
    print(f'#{tc} {max_height - min_height}')