# 2068. 최대수 구하기

T = int(input())

for test_case in range(1, T + 1):
  a, b, c, d, e, f, g, h, i, j = map(int, input().split())
  find_max_list = [a, b, c, d, e, f, g, h, i, j]
  result = max(find_max_list)
  print(f'#{test_case} {result}')