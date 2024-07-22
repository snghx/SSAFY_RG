# 중앙값
# 다시 생각해보기


T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    num = int(test_case // T) + 1
    result = lst[num]
print(result)