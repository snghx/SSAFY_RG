# 파리 퇴치

T = int(input())


def catch(si, sj, M):
    x1, y1, x2, y2 = si, sj, si+M-1, sj+M-1
    ans = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    return ans


for tc in range(1, T+1):
    N, M = map(int, input().split()) # N*N 배열 / M*M 크기의 파리채
    arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    prefix_sum = [[0]*(N+1) for _ in range(N+1)]


# prefix sum 계산
    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix_sum[i][j] = arr[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]


# 쿼리 처리
    ans = 0
    for si in range(1, N-M+2): # si + M -1 <= N
        for sj in range(1, N-M+2):
            temp_ans = catch(si,sj,M)
            ans = max(temp_ans, ans)
    
    print(f'#{tc} {ans}')





''' 옛날에 푼 방식

T = int(input())

def catch(arr, i, j, M):
    ans = 0
    ci, cj = i, j
    for ni in range(ci, i+M):
        for nj in range(cj, j+M):
            ans += arr[ni][nj]
    return ans


for tc in range(1, T+1) :
    N, M = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    ans_max =0
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            p = catch(arr, i, j, M)
            if p > ans_max :
                ans_max = p
    
    print(f'#{tc} {ans_max}')

'''