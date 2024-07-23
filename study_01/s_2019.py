'''2019. 더블더블'''
T = int(input())

for i in range(0, T + 1):
    result = 2 ** i   # 0(2의 1승 = 1)부터 T승까지 출력
    print(result, end = ' ')