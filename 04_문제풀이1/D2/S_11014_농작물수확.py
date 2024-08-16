import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = 10000              # 농작물 총합의 차이 결과 저장 (임시로 큰 값 저장)
    for c in range(1,N):        # 최소 한 구역의 크기가 1 이상이 되어야 하기에, 1부터 N-1 중 구분이 될 지점 정하기
        tmp = 0                 # 구역을 나눈 뒤 최대 - 최소를 기록 
        for r in range(1,N):    # 세로선을 그어서 영역 나누기 ([1,2] / [3])
            # sum1 : 오른쪽 농작물 총합 (그림 속 3번 구역)
            sum1 = 0
            for i1 in range(N):         # 전체 row 순회
                for j1 in range(c,N):   # 세로선 이후부터 끝까지 순회
                    sum1 += arr[i1][j1] # 해당 범위에 속하는 농작물 총합 계산
            # sum2 : 왼쪽(상) 농작물 총합 (그림 속 1번 구역)
            sum2 = 0
            for i2 in range(r):         # 가로선 이전 범위만 순회
                for j2 in range(c):     # 세로선 이전 범위만 순회
                    sum2 += arr[i2][j2] # 해당 범위에 속하는 농작물 총합 계산 
            # sum3 : 왼쪽(하) 농작물 총합 (그림 속 2번 구역)
            sum3 = 0
            for i3 in range(r,N):       # 가로선 이후부터 끝까지 순회
                for j3 in range(c) :    # 세로선 이전 범위만 순회
                    sum3 += arr[i3][j3] # 해당 범위에 속하는 농작물 총합 계산

            # 농작물 총합의 최대 - 최소 계산
            tmp = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)
            
            if result > tmp:  # 최대와 최소 차이가 최소가 되는 경우를 찾아야하기에
                result = tmp  # 더 작은 경우를 발견할 경우 해당 값으로 result 갱신
        
    print(f'#{tc} {result}')