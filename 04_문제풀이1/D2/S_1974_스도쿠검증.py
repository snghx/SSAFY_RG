import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split()))for _ in range(9)]

    num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 비교를 위한 정답 숫자 리스트

    result = 1  # result에 기본 값으로 겹치는 숫자가 없을 경우 출력하는 1 설정

    # (1) 3*3 정사각형 안에 같은 숫자가 있는지 확인 
    for i in range(0,9,3):                  # 각 정사각형의 첫 번째 칸을 기준으로 설정(시작점)
        for j in range(0,9,3):
            tmp1 = []                       # 정사각형 안에 들어있는 숫자들을 넣을 빈 리스트
            for r in range(i, i+3):         # 시작점부터 가로로 3칸을 범위로 설정
                for c in range(j, j+3):     # 시작점부터 세로로 3칸을 범위로 설정
                    tmp1.append(arr[r][c])  # 범위에 속하는 값들을 tmp1에 담기
            tmp1.sort()                     # 비교하기 위해 정렬 
            if tmp1 != num_lst:             # 정답 숫자 리스트와 비교하여 중복 숫자 여부 파악
                result = 0                  # 다를 경우 result 값 변경
    
    # (2) 가로에 같은 숫자가 있는지 확인 (행 순회)
    for r in range(9):
        tmp2 = []                           # 행을 순회하며 값을 넣을 빈 리스트
        for c in range(9):
            tmp2.append(arr[r][c])          # 행을 고정하고 이동하며 가로에 있는 값 tmp2에 담기
        tmp2.sort()                         # 비교하기 위해 정렬
        if tmp2 != num_lst:                 # 정답 숫자 리스트와 비교하여 중복 숫자 여부 파악
            result = 0                      # 다를 경우 result 값 변경
    
    # (3) 세로에 같은 숫자가 있는지 확인 (열 순회)
    for c in range(9): 
        tmp3 = []                           # 열을 순회하며 값을 넣을 빈 리스트
        for r in range(9):
            tmp3.append(arr[r][c])          # 열을 고정하고 이동하며 세로에 있는 값 tmp3에 담기
        tmp3.sort()                         # 비교하기 위해 정렬
        if tmp3 != num_lst:                 # 정답 숫자 리스트와 비교하여 중복 숫자 여부 파악
            result = 0                      # 다를 경우 result 값 변경

    # (1), (2), (3) 단계 검사를 모두 진행한 결과 중복 숫자가 한 번이라도 있었다면 result 값이 0으로 설정되었을 것
    # 정사각형, 가로, 세로 모두 겹치는 숫자가 없을 경우 result 값은 초기 설정대로 1로 유지되었을 것
    
    print(f'#{tc} {result}')
