# 구간 합 구하기 5
# 시작 8:55 .. 못풀어 !!! 안풀어!!!!!!...ㅠ.ㅠ

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for row in range(m)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    sum = 0
