# 2050. 알파벳을 숫자로 변환
# 이건 왜 안 되는 건가요................................. ㅠㅠ

abc = input()

my_list = []

for i in abc :
  my_list.append(i)

for x in range(len(my_list)) :
  print(x + 1 ,end = " ")