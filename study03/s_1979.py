# 1979. 어디에 단어가 들어갈 수 있을까
# 4:08

T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for row in range(n)]

    ans = 0
    #행 순으로 찾기
    for i in range(n):
        point = 0
        for j in range(n):
            if arr[i][j] == 1:
                point += 1
            else:
                if point == k:
                    ans += 1
                point = 0
        if point == k:
            ans += 1

  
    #열 순으로 찾기
    for j in range(n):
        point = 0
        for i in range(n):
            if arr[i][j] == 1:
                point += 1
            else:
                if point == k:
                    ans += 1
                point = 0
        if point == k:
            ans += 1


    print(f'#{t} {ans}')