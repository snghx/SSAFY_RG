# 2072. 홀수만 더하기

T = int(input())

for t in range(1, T+1):
    nums = list(map(int, input().split()))
    ans = sum([x for x in nums if x%2 == 1])
    
    print(f"#{t} {ans}")