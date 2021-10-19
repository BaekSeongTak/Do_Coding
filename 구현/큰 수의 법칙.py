# 배열로 주어진 수들을
# M번 더하여 가장 큰수를 만드는 법칙
# K번을 초과할 수 없다.
# 배열의 특정 인덱스에 해당하는 수가 연속에서 초과할 수 없음.


n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= -1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

