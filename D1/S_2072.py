# 2072.py 홀수더하기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


for test_case in range(1, T+1):
    list_t = list(map(int, input().split()))
    a = []
    for i in list_t:
        if i % 2 != 0:
            a.append(i)
    result = sum(a)
    print(f'#{test_case} {result}')

