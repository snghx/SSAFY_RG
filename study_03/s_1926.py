'''1926. 간단한 369게임 / 50분'''
N = int(input())

for i in range(1, N+1):
    num = str(i)    # N을 문자열로
    count = 0

    for n in num:
        if n == '3' or n == '6' or n == '9': 
        # N을 n으로 하나씩 받아 3,6,9에 해당하는지 확인
            count += 1
    if count > 0:
        print('-' * count, end='')
        # 한 개 이상일 때, -를 출력 / 이후 출력물을 붙임
    else:
        print(num, end='')
        # 없을 때는 수를 출력 / 이후 출력물을 붙임
    
    print(' ', end='')
    # 숫자와 - 사이에 공백을 출력