# 1966번 숫자를 정렬하자
# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라


# sort 버전

# T = int(input())

# for tc in range(1,T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     lst.sort()
#     print(f'#{tc}', *lst)
    
    
# Bubble Sort    
T = int(input())

def Bubblesort(a, N):
    for i in range(N-1,0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                      
    return

                
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    Bubblesort(lst, N)
    print(f'#{tc}', *lst)
    
