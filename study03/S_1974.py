# 스도쿠 검증
 

def check(arr):
    # 가로 확인
    for i in range(9):
        set_i = set()
        for j in range(9):
            if arr[i][j] in set_i:
                return '0'
            else: set_i.add(arr[i][j])
    
    # 세로 확인
    for j in range(9):
        set_j = set()
        for i in range(9):
            if arr[i][j] in set_j:
                return '0'
            else: set_j.add(arr[i][j])
    
    # 9칸 확인하기
    for i in range(0,6,3):
        for j in range(0,6,3):
            set_sq = set()

            for sq_i in range(i, i+3):
                for sq_j in range(j, j+3):
                    if arr[i+sq_i][j+sq_j] in set_sq:
                        return '0'              
                    else: set_sq.add(arr[i+sq_i][j+sq_j] )
    
    return '1'


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = check(arr)
    print(f'#{tc} {ans}')
            