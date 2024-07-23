'''2056. 연월일 달력'''
A = int(input())

for test_case in range(1, A + 1):
    T = input()
    year = T[:4]
    month = T[4:6]
    day = T[6:]
    
    if (month == '01' or month == '03' or month == '05' or month == '07' or 
        month == '08' or month == '10' or month == '12'):   # 31일까지 있는 달
        if 1 <= int(day) <= 31:
            print('#{0} {1}/{2}/{3}'.format(test_case, year, month, day))
        else:
            print('#{0} -1'.format(test_case))
    elif month == '04' or month == '06' or month == '09' or month == '11':
        if 1 <= int(day) <= 30: # 30일까지 있는 달
            print('#{0} {1}/{2}/{3}'.format(test_case, year, month, day))
        else:
            print('#{0} -1'.format(test_case))
    elif month == '02': # 28일까지 있는 2월
        if 1 <= int(day) <= 28:
            print('#{0} {1}/{2}/{3}'.format(test_case, year, month, day))
        else:
            print('#{0} -1'.format(test_case))
    else:
        print('#{0} -1'.format(test_case))

    # 1자리 수인 달(1~9월)인 경우 0N으로 표시해야 해, 위와 같이 가져옴