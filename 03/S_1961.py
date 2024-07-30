# 1961. 숫자 배열 회전 (40m)

T = int(input())

for tc in range(1, T+1) :
    n = int(input())

    # 값을 입력받아 n*n 행렬 만들기
    # 회전한 모양을 출력하기 위해 문자열로 지정
    arr = [list(map(str, input().split()))for i in range(n)]

    # 회전한 값을 저장하기 위해 행렬 만들기 (90 / 180 / 270)
    arr_90 = [[0]*n for i in range(n)]
    arr_180 = [[0]*n for i in range(n)]
    arr_270= [[0]*n for i in range(n)]

    # 회전한 값을 각 행렬에 입력(1) - 90도 회전
    for i in range(n) :
        for j in range(n) :
            arr_90[j][n-i-1] = arr[i][j]

    # 회전한 값을 각 행렬에 입력(2) - 180도 회전
    for i in range(n) :
        for j in range(n) :
            arr_180[j][n-i-1] = arr_90[i][j]

    # 회전한 값을 각 행렬에 입력(3) - 270도 회전
    for i in range(n) :
        for j in range(n) :
            arr_270[j][n-i-1] = arr_180[i][j]

    # 회전한 정보를 담은 행렬 출력하기
    print(f'#{tc}')
    for i in range(n) :
        print("".join(arr_90[i]), "".join(arr_180[i]), "".join(arr_270[i]))
