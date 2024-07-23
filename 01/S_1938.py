# 1938. 아주 간단한 계산기

x, y = map(int, input().split())

def my_calculator(x,y) :
    print(x + y)
    print(x - y)
    print(x * y)
    print(x // y)

print(my_calculator(x,y))