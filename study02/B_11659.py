# 구간 합 구하기 4

N, M = map(int, input().split())

nums = list(map(int, input().split()))

# 누적 합 구하기
prefix_sum = [0]
temp = 0
for i in nums :
    temp = temp + i
    prefix_sum.append(temp)

for _ in range(M):
    s, e = map(int, input().split())
    ans = prefix_sum[e]- prefix_sum[s-1]    
    
    print(ans)
    