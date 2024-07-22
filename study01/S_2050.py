# 알파벳을 숫자로 변환

string = input()

list_a = [ord(s)-64 for s in string]
print(*list_a)
