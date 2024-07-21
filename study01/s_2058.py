# 2058. 자릿수 더하기

num = input() #input이 10이라면, 1,0 순으로 순회해야 하니까 int가 아니라 str으로 저장
ans_sum = 0 

for n in num:
    ans_sum += int(n)
    
print(ans_sum)