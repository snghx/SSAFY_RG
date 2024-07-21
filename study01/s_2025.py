# 2025. N줄덧셈

num = int(input())

#ver1 : ans_sum 변수 만들어서 하나하나 저장하기
ans_sum = 0
for i in range(1, num+1):
    ans_sum += i
print(ans_sum)

#ver2 : list comprehension 사용
ans = sum([x for x in range(1, num+1)])
print(ans)