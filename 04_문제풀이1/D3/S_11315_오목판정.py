import sys
sys.stdin = open("input.txt")

dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    omok = [input() for _ in range(N)]
 
    # 오목 판정을 위한 함수 만들기
    def omok_check(arr, n):
        for i in range(n):
            for j in range(n):
 
                if arr[i][j] == 'o':
                    for k in range(4):
                        cnt = 1
                        for l in range(1, 5):
                            ni = i + dr[k] * l
                            nj = j + dc[k] * l
                            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                                cnt += 1
                            else:
                                break
 
                        if cnt == 5:
                            return 'YES'
 
        return 'NO'
 
    result = omok_check(omok, N)

    print(f'#{tc} {result}')

                            

