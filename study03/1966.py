# 숫자를 정렬하자


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list_a = list(map(int, input().split()))
    list_a.sort()

    print('#', tc, *list_a)


'''
T = int(input())
for test_case in range(1, 1+T):
    
    N = int(input())
    list_a = list(map(int, input().split()))
	
    print(f'#{test_case}', end=' ')
    
    for i in range(1, N+1):
        m = min(list_a)
        list_a.remove(m)
        print(m, end=' ')
        
    print()
'''
