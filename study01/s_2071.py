# 2071. 평균값 구하기

T = int(input())

for t in range(1, T+1):
    nums = list(map(int, input().split()))
    ans = round(sum([x for x in nums]) /10, 0)
    
    print(f"#{t} {ans:.0f}")