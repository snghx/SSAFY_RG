import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    mid = n//2
    s = e = mid

    result = arr[0][mid]

    for r in range(n):
        if r < mid:
            s, e = s-1, e+1
            for i in range(s):
                for j in range()

