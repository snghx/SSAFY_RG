# 1936. 1대1 가위바위보

a, b = map(int, input().split())

'''
가위 = 1
바위 = 2
보 = 3

가위 - 바위 : 바위 (1, 2 => 2)
가위 - 보 : 가위 (1, 3 => 1)
바위 - 보 : 보 (2, 3 => 3)
'''

if (a==2 and b ==1) or (a==1 and b==3) or (a==3, b==2): # a가 이기는 경우의 수 (위 str 참고 ~)
    print('A')
else:
    print('B')