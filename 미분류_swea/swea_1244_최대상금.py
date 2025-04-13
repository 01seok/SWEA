def dfs(swap_cnt):
    global max_money
    
    # 종료 조건 : 입력 받은 스왑 횟수만큼 스왑했다면 종료
    if swap_cnt == total_swap_cnt:
        # 숫자판은 리스트로 받았으니 정수 형태로 변환해서 갱신
        max_money = max(max_money, int(''.join(nums)))
        return

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            # 현황판 길이 만큼 순회하며 앞뒤로 스왑을 진행한 후
            str_nums = ''.join(nums)    # 문자열 숫자판 공백없이 결합
            if visited.get((swap_cnt, str_nums)) is None:   # 그 스왑 횟수의 그 숫자판이 아니었다면 visited에 추가하고
                visited[(swap_cnt, str_nums)] = 1   # 방문 기록하고
                dfs(swap_cnt + 1)   # 재귀 호출해서 다음으로
            
            nums[i], nums[j] = nums[j], nums[i] # 다른 경우의 수 탐색하기 위해 원상복구

T = int(input())
for tc in range(1, T + 1):
    nums, total_swap_cnt = input().split()    # 숫자판 현황과 총 스왑 할 횟수
    nums = list(nums)   # 숫자판은 리스트 형태로
    total_swap_cnt = int(total_swap_cnt)    # 스왑 횟수는 정수로
    max_money = -1 # 최대 상금, 음수는 될 수 없으니
    
    visited = {}    # 중복 처리 피하기 위한 visited, 몇번째 swap에 어떤 숫자가 왔는지 확인
    dfs(0)
    print(f'#{tc} {max_money}')