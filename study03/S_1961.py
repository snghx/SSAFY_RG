# 숫자 배열 회전 

def rotate(arr):
    new_arr = [[0]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-j-1][i]
    return new_arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    arr1 = rotate(arr)
    arr2 = rotate(arr1)
    arr3 = rotate(arr2)

    for a, b, c in zip(arr1, arr2, arr3):
        print(f'{"".join(map(str,a))} {"".join(map(str,b))} {"".join(map(str,c))}')