# n,m(행,열)
# 행을 기준으로 선택한 카드 중 가장 숫자가 작은 카드를 하나씩 뽑고,
# 각 행의 가장 작은 숫자 카드 중 가장 큰 수를 출력

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)
    result = max(result, min_value)

print(result)