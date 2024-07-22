# 간단한 소인수분해

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print('#{}'.format(test_case), end=' ')
    for i in [2,3,5,7,11]:  # prime factorization 리스트 만들기
        cnt = 0
        while N % i == 0:
            N //= i
            cnt += 1
        print(cnt, end=' ')
    print()