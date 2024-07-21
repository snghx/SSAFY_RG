# 1545. 거꾸로 출력해 보아요

n = int(input())
ans_list = [x for x in range(n, -1, -1)] # range(n, m, -1) : n부터 m까지 -1씩 줄어들며 역순으로 수행 (n>m)

print(ans_list)