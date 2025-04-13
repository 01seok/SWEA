# swea_GNS

T = int(input())

planet = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    
    tn, N = input().split() # 테스트 케이스 번호, 단어의 갯수
    arr = input().split() # 단어들을 공백기준 분리하여 리스트 저장
    
    counts = [0] * 10 # planet 리스트 단어들 등장 횟수 저장할 곳
    
    for word in arr:
        counts[planet.index(word)] += 1 # 단어들의 인덱스를 찾은 후 그 위치에 카운트 1씩 증가시켜 갯수 찾기
    
    result = [] # 정렬 결과 저장할 리스트 생성 (출력할)
    
    for i in range(10):
        result.extend([planet[i]] * counts[i]) # planet[i]를 갖고있는 리스트 등장 횟수 곱하면 몇번 반복하는지 알 수 있음
        # 리스트별로 출력하는게 아니라 한 리스트에 담아야하므로 extend 사용
    
    print(tn)
    print(" ".join(result)) # 공백으로 구분하여 리스트 출력
    
    
    
    # swea_GNS

T = int(input())

planet = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

# 테스트 케이스 번호, 단어의 갯수
tn, N = int(input())
# 단어들을 공백기준 분리하여 리스트 저장
arr = input().split()
# planet 리스트 단어들 등장 횟수 저장할 곳
counts = [0] * 10
# 단어들의 인덱스를 찾은 후 그 위치에 카운트 1씩 증가시켜 갯수 찾기
for word in arr:
    counts[planet.index(word)] += 1
# 정렬 결과 저장할 리스트 생성 (출력할)
result = []
# planet[i]를 갖고있는 리스트 등장 횟수 곱하면 몇번 반복하는지 알 수 있음 , # 리스트별로 출력하는게 아니라 한 리스트에 담아야하므로 extend 사용
for i in range(10):
    result.extend[planet[i] * counts[i]]
# 공백으로 구분하여 리스트 출력