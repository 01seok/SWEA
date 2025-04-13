for tc in range(10):
    tc = input().split()[0]
    
    arr = [list(input()) for _ in range(100)]
    max_lenth = 1 # 회문 최대 길이
    
    for i in range(100):
        for j in range(100):
            m = 1 # 회문 길이, 1부터 인정
            while j + m <= 100:
                for k in range(m // 2):
                    if arr[i][j+k] != arr[i][j+m-1-k]:
                        break
                else:
                    max_lenth = max(max_lenth, m) # 회문 최대 길이 갱신
                    
                m += 1 # 다음 길이 찾으러 가기
    
    for j in range(100):
        for i in range(100):
            m = 1
            while i + m <= 100:
                for k in range(m // 2):
                    if arr[i+k][j] != arr[i+m-1-k]:
                        break
                else:
                    max_lenth = max(max_lenth, m)
                    
                m += 1
                
    print(f'{tc} {max_lenth}')