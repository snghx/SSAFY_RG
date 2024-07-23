'''1936. 1대1 가위바위보'''
A, B = list(map(int, input().split()))

if A == 1:  # A가 1(가위)일 때, 경우의 수
    if B == 2:
        print("B")
    elif B == 3:
        print("A")
elif A == 2:    # A가 2(바위)일 때, 경우의 수
    if B == 1:
        print("A")
    elif B == 3:
        print("B")
elif A == 3:    # A가 3(보)일 때, 경우의 수
    if B == 1:
        print("B")
    elif B == 2:
        print("A")