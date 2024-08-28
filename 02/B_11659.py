# 11659. 구간 합 구하기 4

n,t = list(map(int, input().split()))

n_list = list(map(int, input().split()))

# print(n_list)


for test_case in range(1, t+1) :
    i, j = map(int,input().split())
    tmp = i-1
    sum_list = []
    while tmp != j :
        sum_list.append(n_list[tmp])
        tmp += 1
    print(sum(sum_list))


