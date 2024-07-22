'''1545. 거꾸로 출력해 보아요'''
T = int(input())

for i in range(0, T + 1):
    print(T, end = ' ')    # T부터 출력 / T, T-1 ... T-T까지
    T -= 1