# 1961. 숫자 배열 회전
# 10:39

def rotate(array, n):
    temp = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            temp[i][j] = array[n-j-1][i]

    return temp


T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr90 = rotate(arr, n)
    arr180 = rotate(arr90, n)
    arr270 = rotate(arr180, n)

    total = zip(arr90, arr180, arr270)
    print("".join(map(str, *total)))