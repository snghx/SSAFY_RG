# 2063. 중간값 찾기

N = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
print(n_list[N//2])