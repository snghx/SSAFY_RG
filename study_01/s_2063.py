'''2063. 중간값 찾기'''
N = int(input())

num = list(map(int, input().split()))
num.sort()

result = num[N//2] # 중간값인 경우 2로 나눈 후 +1를 해야하지만, 0부터 시작이라 생략
print(result)