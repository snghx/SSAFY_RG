# 1대1 가위바위보

a, b = list(map(int, input().split()))

# a가 이기는 조건 : 1>3, 2>1, 3>2

if a == 1 and b ==3:
    print("A")
elif a == 2 and b == 1:
    print("A")
elif a == 3 and b == 2:
    print("A")
else:
    print("B")

