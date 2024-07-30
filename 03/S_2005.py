# 2005. 파스칼의 삼각형 (60m)

T = int(input())

for tc in range(1, T+1) :
    n = int(input())

    result_list = []

    for i in range(n) :
        row = [1] * (i+1)
        if i > 1 :
            for j in range(1, i) :
                # 바로 이전 행 값 2개 (위, 위-오른쪽) 더해서 값 계산 후 변경
                row[j] = result_list[i-1][j] + result_list[i-1][j-1]
        result_list.append(row)
    
    print(f'#{tc}')
    for row in result_list :
        print(" ".join(map(str,row)))


