# 1959. 두 개의 숫자열
# 9:28 시작 (-3분) 9:55종료 17분

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    '''
    n과 arr1이 짧은 부분
    m과 arr2가 긴 부분
    '''
    
    if n > m:
        n, m = m, n
        arr1, arr2 = arr2, arr1
    
    ans_sum = []
    for i in range(m-n+1):
        temp = []
        for j in range(n):
            temp.append(arr1[j] * arr2[i+j])
        ans_sum.append(sum(temp))
    
    print(f"#{t} {max(ans_sum)}")