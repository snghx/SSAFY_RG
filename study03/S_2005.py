# 파스칼의 삼각형

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    arr = [[0] * i for i in range(1, N+1)]  # ex. [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]

    for i in range(N):
        arr[i][0] = 1
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        arr[i][i] = 1

    print(f'#{tc}')
    for row in arr:
        # print(" ".join(map(str, row)))
        print(*row)