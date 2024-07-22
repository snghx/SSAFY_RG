'''2050. 알파벳을 숫자로 변환'''
T = input()

for test_case in T:
    print(ord(test_case)-64, end = ' ') 

# ord() : 유니코드로 변환
# print(ord('A')) # 65