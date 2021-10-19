# 어떤 수 n이 1이 될 때까지 다음 2 과정 중 하나를 반복적으로 선택하여 수행
# 단, 2번째 연산은 n이 k로 나누어떨어질 때만 선택 가능
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)