# 구간 합 구하기 5 (44m) - 시간초과래요...

N,M = list(map(int,input().split()))

# N*N matrix 만들기
my_matrix = [list(map(int, input().split())) for i in range(N)]

for test_case in range(1, M+1) : # M번 test_case 반복
    x1, y1, x2, y2 = map(int, input().split()) # 입력된 값을 각각 x1, y1, x2, y2로 지정

    my_list = [] # 합계를 더할 빈 리스트 생성

    for x in range(x1,x2+1): # my_matrix에서 값을 더할 때 활용할 x 범위 지정.
        for y in range(y1, y2+1): # my_matrix에서 값을 더할 때 활용할 y 범위 지정.
            my_list.append(my_matrix[x-1][y-1]) # 범위에 해당하는 my_matrix의 값들만 my_list에 저장
    print(sum(my_list)) 

