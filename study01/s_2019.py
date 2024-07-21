# 2019. 더블더블

n = int(input())
ans_list = [2**x for x in range(1, n+1)] # 2의 n제곱을 ans_list에 저장, 근데 이제 n = 1, 2, 3...n
print(*ans_list)