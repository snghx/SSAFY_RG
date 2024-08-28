# 구간 합 구하기 5

n,m = list(map(int, input().split()))

# 입력 값을 활용하여 행렬 만들기
arr = [[0]*(n+1)]
arr2 = [[0] * (n+1) for _ in range(n+1)]

for i in range(n) :
    arr_row = [0] + [int(x) for x in input().split()]
    arr.append(arr_row)

# 구간 합 만들기
for i in range(1,n+1) :
    for j in range(1, n+1) :
        arr2[i][j] = arr2[i][j-1] + arr2[i-1][j] + arr2[i-1][j-1] + arr[i][j]

for _ in range(m) :
    a, b, c, d = map(int, input().split())
    result = arr2[c][d] - arr2[a-1][d] - arr2[c][b-1] + arr2[a-1][b-1]
    print(result)



