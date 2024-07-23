# 2043. 서랍의 비밀번호

# p가 k 보다 큰 예시 경우 이외에도 작은 경우를 함께 고려 필요

p, k = map(int, input().split())

def my_password(p, k) :
  if p >= k :
    return p-k+1
  else :
    return 1000 - k + p + 1

print(my_password(p,k))