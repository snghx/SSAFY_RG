# 2029. 몫과 나머지 출력하기

# 여러 개의 테스트 케이스가 주어지는 경우 다음과 같이 작성

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    x = a//b
    y = a%b
    print(f'#{test_case} {x} {y}')