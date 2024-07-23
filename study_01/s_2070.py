'''2070. 큰 놈, 작은 놈, 같은 놈'''
T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    if num[0] > num[1]: # 먼저 오는 수가 클 경우 '>'
        print(f"#{test_case} >")
    elif num[0] < num[1]:   # 뒤의 수가 클 경우 '<'
        print(f"#{test_case} <")
    else:   # 둘 다 아닌, 같은 경우 '='
        print(f"#{test_case} =")