# 1545. 거꾸로 출력해 보아요 (9m)

num = int(input())

my_countdown = []

for i in range(1, num+2) :
    my_countdown.append(num)
    num = num-1
    my_countdown_str = map(str, my_countdown)
    result = " ".join(my_countdown_str)

print(result)