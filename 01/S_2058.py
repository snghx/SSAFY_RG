# 2058. 자릿수 더하기

num = int(input())

def my_cal_sum(num):
  if num < 10 :
    return num
  else :
    return (num % 10) + my_cal_sum(num // 10)

print(my_cal_sum(num))