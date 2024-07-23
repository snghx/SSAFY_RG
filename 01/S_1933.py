# 1933. 간단한 N의 약수

N = int(input())

tmp = []

for i in range(1, N+1) :
  if N % i == 0 :
    tmp.append(i)
  else :
    pass
tmp_result = list(map(str,tmp))
result = " ".join(tmp_result)
print(result)