# 중간값 찾기

N = int(input())
list_a = list(map(int, input().split()))
list_a.sort() # 정렬하기


M = (N+1)//2 # 중간값이 몇번째 값인지: '/'로 하게 되면 6/2 = 3.0 
ans = list_a[M-1] # 0번째부터 시작하니까 -1

print(ans)


