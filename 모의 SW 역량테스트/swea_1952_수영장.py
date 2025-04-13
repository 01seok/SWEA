def recur(month, total_fee):
    global min_fee
    
    if min_fee < total_fee: # 이미 갱신되어 있는 최소 요금보다 비싸지면 볼 필요 없음
        return

    if month > 12:
        min_fee = min(min_fee, total_fee)
        return
    
    # 일권, 월권, 3개월권, 1년권 다 비교 해보기
    recur(month + 1, total_fee + (dayily_pass * schedule[month]))
    recur(month + 1, total_fee + month_pass)
    recur(month + 3, total_fee + month3_pass)
    recur(month + 12, total_fee + year_pass)


T = int(input())
for tc in range(1, T + 1):
    dayily_pass, month_pass, month3_pass, year_pass = map(int, input().split())
    
    # 매 월 이용 계획표, 1월부터인데 인덱스는 0번부터이니 앞에 0 하나 추가해주기
    schedule = [0] + list(map(int, input().split()))
    min_fee = float('inf')
    recur(1, 0)
    print(f'#{tc} {min_fee}')