# 최대수 구하기

T = int(input())

for tc in range(1, T+1):
    list_a = list(map(int, input().split()))

    ans = max(list_a)
    print(f'#{tc} {ans}')