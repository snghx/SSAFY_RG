# r = c = 0
# for i in range(100):...
#     dir = 1 # 0: 왼 1 : 위 2 : 오른쪽
#     while r > 0:
#         # 현재 r,c 에서 이동
#         # 왼쪽
#         if c -1 >= 0  and arr[r][c-1] ==1:
#             while c -1 >= 0  and arr[r][c-1] ==1:
#                 c -= 1    
#         #오른족
#         elif c+1 < 100 and arr[r][c+1] == 1:
#             while c -1 >= 0  and arr[r][c-1] ==1:
#                 c += 1
#         #위쪽
#     r -= 1
# print(c)


import sys; sys.stdin = open('1210_ladder.txt')


def finding_start_point(ladder, r, c):
    ladder[r][c] = 0
    # 같은 경로로 돌아가지 않도록 벽으로 만듦
    if r == 0:
        # 꼭대기에 올라갔을때
        return c
    
    retrn = 0
    if c > 0 and ladder[r][c - 1] == 1:
        # c - 1 왼쪽으로 가니까 작아질 수 밖에 없지.
        # 긘까 c가 0보다 작거나 같아질 경우만 제외
        retrn = finding_start_point(ladder, r, c -1)
    elif c < 99 and ladder[r][c+1] == 1:
        # c+1 오른쪽으로 가니까 커질수 밖에 없지.
        # 긘까 c가 99보다 큰, 영역 밖으로 나가지 않으면 됨.
        retrn = finding_start_point(ladder, r, c+1)
    else:
        # 영역 밖으로 나가거나 더이상 길이 양옆에 없을때
        # 우리는 2부터 시작했으니까 위로 올라가야지
        retrn = finding_start_point(ladder, r-1, c)
    ladder[r][c] = 1
    # 탐색이 끝난뒤, 다음 시도에서 이 방향이 길인걸 인지할 수 있도록.
    # 다시 원상태로 복구하는 것.
    # rc가 = 0 이면 
    return retrn


for tc in range(1, 11):
    tc_num = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    r = c = 0
    for i in range(100):
        if ladder[99][i] ==2:
            r,c  = 99, i
            break

    ans = finding_start_point(ladder, r,c)
    
    print(f'#{tc} {ans}')
    


