# 2019. 더블더블 (22m)

num = int(input())


my_list = [1,]

for i in range(1, num+1) :
  i = my_list[i-1]*2
  my_list.append(i)

my_list_str = map(str, my_list)
result = " ".join(my_list_str)

print(result)