# 2050번 알파벳을 숫자로 변환

# 어려웠던 점 : 아스키 코드 사용
# 아스키코드 : 65~90
# 아스키코드 숫자 변환 : ord("알파벳")

T = str(input())

alpha = []
for i in T:
    a = int(ord(i)) - 64
    alpha.append(a)

for i in alpha:
    print(i, end = " ")
    