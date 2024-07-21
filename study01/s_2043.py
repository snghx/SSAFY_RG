# 2043. 서랍의 비밀번호

key, start = map(int, input().split())

#ver1
print(key - start + 1)

# ver2
cnt = 1
while start != key: #시작값과 비밀번호가 같을 때까지 while문 수행
    start += 1
    cnt += 1
    
print(cnt)