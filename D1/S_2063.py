# 중앙값
# 다시 생각해보기
# 왜 안될까... 자고일어나서 다시 생각하기...


T = int(input())

lst = list(map(int, input().split()))
lst.sort()
num = int(T // 2)
result = lst[num]
print(result)