# 1933. 간단한 N 의 약수

n = int(input())
ans_list = []

for i in range(1, n+1):
    if n%i == 0: #나머지가 0이면, 약수이므로
        ans_list.append(i) #리스트에 추가

print(*ans_list) #리스트 언패킹해서 출력