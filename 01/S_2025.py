# 2025. N줄 덧셈

num = int(input())

def my_sum() :
    if num == 1 :
        return 1
    else :
        return num + my_sum(num-1)

print(my_sum())