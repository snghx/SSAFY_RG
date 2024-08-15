T = int(input())
 
for tc in range(1, T+1):
    n = int(input())
    carrots = list(map(int, input().split()))
 
    max_cnt = 0
    for i in range(n):
        cnt = 1
        for j in range(i, n-1):
            if carrots[j] < carrots[j+1]:
                cnt += 1
            else :
                break
        if max_cnt < cnt :
            max_cnt = cnt
     
    print(f'#{tc} {max_cnt}')