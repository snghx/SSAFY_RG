# 1545번 거꾸로 출력

# 주의점 : range(시작점, 종착역 미포함, 방향)


N = int(input())

for test_case in range(N, -1, -1):
    print(test_case, end = " ")

