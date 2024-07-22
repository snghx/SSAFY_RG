# 1986. 지그재그 숫자

T = int(input())

for t in range(1, T+1):
    n = int(input())
    odd_sum = 0
    even_sum = 0
    
    for i in range(1, n+1):
        if i%2 == 0:
            even_sum += i
        else:
            odd_sum += i
    print(f"#{t} {odd_sum - even_sum}")