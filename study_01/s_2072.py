'''2072. 홀수만 더하기'''
t = int(input())

for test_case in range(1, t + 1):
    odd = list(map(int, input().split()))
    result = 0
    for i in odd:
        if i % 2 == 1:  # 2로 나누었을 때 나머지가 1
            result += i # result = 0부터 홀수인 수를 더함
    print(f'#{test_case} {result}')