T = int(input())
for tc in range(1, T + 1):
    dayily_pass, month_pass, month3_pass, year_pass = map(int, input().split())
    # 매 월 이용 계획표, 1월부터인데 인덱스는 0번부터이니 앞에 0 하나 추가해주기
    schedule = [0] + list(map(int, input().split()))
    
    dp = [0] * 13
    
    # 시작점 초기화 (1월, 2월)
    dp[1] = min(schedule[1] * dayily_pass, month_pass)
    # 2월의 가격은 1월의 가격 + 1일권 구매 vs 1달권 구매
    dp[2] = dp[1] + min(schedule[2] * dayily_pass, month_pass)
    
    # 3월부터 12월은 반복하며 계산
    for month in range(3, 13):
        # 3월의 최소 비용
        # 1. 1월에 3개월 이용권을 구매한 경우
        # 2. 2월의 최소 비용 + 1일권 구매 한 경우
        # 3. 2월의 최소 비용 + 1달권 구매 비용
        
        # 1번의 경우 N-3월
        # 2,3번의 경우 바로 이전 월이니 N-1월
        dp[month] = min(dp[month - 3 ] + month3_pass,
                        dp[month - 1] + schedule[month] * dayily_pass,
                        dp[month - 1] + month_pass)
    # 12월의 누적 최소 금액 vs 1년권
    answer = min(dp[12], year_pass)
    print(f'#{tc} {answer}')

'''

    DP 문제 접근법
# Top - Down 방식
- DP (메모이제이션)
- 거듭제곱 문제

# Bottom - Up 방식
- 시작점을 정해두고 앞으로 쌓아나가면서 진행
- 기존 값을 활용
- 정답이 될 수 있는 값(최소 최대 등)을 계산해서 저장하면서 진행
-> 점화식을 구하는 경우가 많다

'''