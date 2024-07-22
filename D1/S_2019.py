# 2019번 더블더블

# 2를 곱한 값들 ; 제곱

T = int(input())

lst = []
for i in range(T+1):
    a = 2 ** i
    lst.append(a)

for n in lst:
    print(n, end = ' ')

