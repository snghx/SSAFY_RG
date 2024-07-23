'''2047. 신문 헤드라인'''
T = input()

for test_case in T:
    if 65 <= ord(test_case) <= 90:
        print(test_case, end='')
    elif 97 <= ord(test_case) <= 122:
        print(test_case.upper(), end='')
    else:
        print(test_case, end='')
    

# print(ord('A')) # 65
# print(ord('Z')) # 90
# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('_')) # 95