# 2071. 평균값 구하기 (10m)

T = int(input())

for test_case in range(1, T+1) :
  numbers = map(int, input().split())
  my_list = []
  for i in numbers :
    my_list.append()
    my_list_sum = sum(my_list)
    result = int(round(my_list_sum / 10,0))
  print(f'#{test_case} {result}')