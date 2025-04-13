T = int(input())  # 테스트 케이스의 수를 입력받음

for tc in range(1, T+1):  # 각 테스트 케이스마다 반복
    N = int(input())  # 카드의 개수 N을 입력받음
    cards = input().split()  # 카드 이름들을 공백으로 구분하여 리스트에 저장

    # 카드 덱을 두 부분으로 나눔
    if N % 2 == 0:  
        # N이 짝수인 경우: 정확히 반으로 나눌 수 있음
        first_half = cards[:N // 2]   # 첫 번째 절반: 앞쪽 N/2장의 카드
        second_half = cards[N // 2:]    # 두 번째 절반: 나머지 N/2장의 카드
    else:
        # N이 홀수인 경우: 먼저 놓는 쪽(첫 번째 절반)에 카드가 한 장 더 많아짐
        first_half = cards[: (N + 1) // 2]  # 첫 번째 절반: (N+1)//2장의 카드
        second_half = cards[(N + 1) // 2:]    # 두 번째 절반: 나머지 카드

    result = []  # 퍼펙트 셔플 결과를 저장할 리스트

    # 두 절반의 카드를 교대로 합침
    # 두 번째 절반의 길이만큼 반복 (두 번째 절반에 있는 모든 카드에 대해)
    for i in range(len(second_half)):
        result.append(first_half[i])   # 먼저 첫 번째 절반의 i번째 카드 추가
        result.append(second_half[i])  # 그 다음 두 번째 절반의 i번째 카드 추가

    # 만약 N이 홀수인 경우, 첫 번째 절반에 카드가 한 장 더 있으므로 그 카드를 결과에 추가
    if len(first_half) > len(second_half):
        result.append(first_half[-1])  # 첫 번째 절반의 마지막 카드 추가

    # 테스트 케이스 번호와 결과를 출력 (카드 이름들을 공백으로 구분)
    print(f"#{tc}", " ".join(result))