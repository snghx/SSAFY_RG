# 2027. 대각선 출력하기

# print('#++++')
# print('+#+++')
# print('++#++')
# print('+++#+')
# print('++++#')

for i in range(0,5) :
  my_list = ['+', '+', '+', '+']
  my_list.insert(i, '#')
  result = "".join(my_list)
  print(result)