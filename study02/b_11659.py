# 구간 합 구하기4

n_data, q_data = map(int, input().split())
arr = list(map(int, input().split()))

for q in range(q_data):
    i, j = map(int, input().split())
    
    sum = 0
    for idx in range(i, j+1):
        sum += arr[idx-1]
    
    print(sum)