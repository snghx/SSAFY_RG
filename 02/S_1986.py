# 1986. 지그재그 숫자 (8m)

T = int(input())

for test_case in range(1, T+1) :
    num_list = []
    num = int(input())

    for i in range(1, num+1) :
        num_list.append(i)

    for j in range(1, num+1) :
        if j % 2 == 0:
            num_list[j-1] = - num_list[j-1]
    
    result = sum(num_list)
    print(f'#{test_case} {result}')
