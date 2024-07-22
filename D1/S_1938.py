#1938번 아주 간단한 계산기
import math
from math import floor

a, b = map(int, input().split())


def cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(floor(a/b))
    return

result = cal(a,b)

print(result)