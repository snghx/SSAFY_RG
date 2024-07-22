#평균값구하기



T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    result = round(sum(lst) / len(lst))



    print(f'#{test_case} {result}')