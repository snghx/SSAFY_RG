# 2029번 몫과 나머지 출력하기

T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    q = lst[0] // lst[1]
    r = lst[0] % lst[1]
    print(f'#{test_case} {q} {r}')
