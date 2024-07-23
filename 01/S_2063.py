# 2063. 중간값 찾기 (25m)

N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

m_pos = (N //2)

result = numbers[m_pos]

print(result)