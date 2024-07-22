# 2070번 큰, 작, 같은 놈


T = int(input())


for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    i = lst[0]
    k = lst[1]
    if i > k:
        result = ">"
    elif i < k:
        result = "<"
    else:
        result = "="

    print(f'#{test_case} {result}')