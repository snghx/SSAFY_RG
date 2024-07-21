# 2068. 최대수 구하기

T = int(input())

for t in range(1, T+1):
    nums = list(map(int, input().split()))
    ans = max([x for x in nums])
    
    print(f"#{t} {ans}")