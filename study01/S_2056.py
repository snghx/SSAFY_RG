# 연월일 달력

# 달력 딕셔너리 만들기
day = {'01': '31', '02': '28', '03': '31', '04': '30', '05': '31', '06': '30',
'07':'31', '08': '31', '09':'30', '10':'31', '11':'30', '12':'31'}

T = int(input())

for tc in range(1, T+1):
    YMD = input()
    y, m, d = YMD[:4], YMD[4:6], YMD[6:8]  # 년(y), 월(m), 일(d)

    # 'm'이 달력의 달에 포함이 안될 경우 / 'd'가 해당 달의 값 이상일 경우 or 자연수가 아닐 경우 => -1
    if (m not in day.keys()) or (int(d) > int(day[m]) or int(d) < 1): 
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {y}/{m}/{d}')





''' 방법2: 달 특징마다 if문
T = int(input())

for test_case in range(1, T + 1):
    tc = str(input())
    y = tc[0:4]
    m = tc[4:6]
    d = tc[6:8]
    if int(m) < 13 and int(m) > 0 and int(d) > 0:
        if m == '02':
            if int(d) < 29:
                print('#{} {}/{}/{}'.format(test_case,y,m,d))
            else: print('#{} -1'.format(test_case))
        elif m in ['04', '06', '09', '11']:
            if int(d) < 31:
                print('#{} {}/{}/{}'.format(test_case,y,m,d))
            else: print('#{} -1'.format(test_case))
        
        else:
            if int(d) <= 31:
            	print('#{} {}/{}/{}'.format(test_case,y,m,d))
            else: print('#{} -1'.format(test_case))
 
    else:
        print('#{} -1'.format(test_case))
              
                   
'''


