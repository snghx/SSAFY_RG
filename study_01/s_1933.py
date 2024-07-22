'''1933. 간단한 N의 약수'''
T = int(input())

for i in range(1, T + 1):
    if T % i == 0:  # 1부터 T까지 나누었을 때, 나머지가 0
        print(i, end = ' ')