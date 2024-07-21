# 홀수만 더하기

T = int(input())

for tc in range(1, T+1):
    list_a = list(map(int, input().split()))

    list_temp = [i for i in list_a if i % 2 == 1]
    ans = sum(list_temp)

    print(f'#{tc} {ans}')



'''
T = int(input())

for test_case in range(1, T + 1):
    
list_n = list(map(int, input().split()))
sum = 0
    
for num in list_n:
    if num % 2 == 1 :
        sum += num
     
print('#' + str(test_case) + ' ' + str(sum)) 
'''