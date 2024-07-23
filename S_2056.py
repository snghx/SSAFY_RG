#2056번 연월일 달력

T = int(input())

oddmonth = [1,3,5,7,8,10,12]
evenmonth = [4,6,9,11]
feb = [2]


for test_case in range(1, T + 1):
    is_vaild = True
    cal = input()
    year = cal[0:4]
    month = cal[4:6]
    day = cal[6:]

    # print(int(month))
    # print(int(year))
    # print(int(day))

    if int(day) < 1:
        is_vaild = False
    if int(month) < 1:
        is_vaild = False
    if int(month) in oddmonth and int(day) > 31:
        is_vaild = False
    if int(month) in evenmonth and int(day) > 30:
        is_vaild = False
    if int(month) in feb and int(day) > 28:
        is_vaild = False
    
    if is_vaild == True:
        print(f'#{test_case} {year}/{month}/{day}')
    else:
        print(f'#{test_case}-1')


