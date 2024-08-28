import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))

    result = 0
    if N <= M:
        for i in range(M-N+1):
            tmp = 0
            for j in range(N):
                tmp += lst_a[j]*lst_b[i+j]
            if result < tmp:
                result = tmp
    else:
        for i in range(N-M+1):
            tmp = 0
            for j in range(M):
                tmp += lst_a[i+j]*lst_b[j]
            if result < tmp:
                result = tmp
    
    print(f'#{tc} {result}')
                