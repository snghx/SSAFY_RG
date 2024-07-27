# 간단한 369게임


N = int(input())

for num in range(1, N+1):
    cnt = 0
    for s in str(num):
        if int(s) != 0 and int(s) % 3 == 0 :  # ex. 10인 경우 1, 0 -> 0을 3으로 나눠도 0
            cnt +=1
    
    if cnt >= 1:
        print('-' *cnt, end= ' ') 
    else:
        print(str(num), end= ' ')