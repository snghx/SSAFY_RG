# 1966. 숫자를 정렬하자
# 3:38시작

T = int(input())

for t in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    print(f"#{t}", *nums)