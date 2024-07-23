# 2056. 연월일 달력

T = int(input())

for test_case in range(1, T+1):
  my_date = list(input())                 # 리스트로 날짜 받아오기

  my_year = my_date[0:4]                  # 날짜에서 year에 해당하는 부분만 추출
  my_year_str = "".join(my_year)          # join을 활용해 출력 시 활용할 문자열 생성


  my_month = my_date[4:6]                 # 날짜에서 month에 해당하는 부분만 추출
  my_month_int = int("".join(my_month))   # 값 비교를 위해 int로 변경
  my_month_str = "".join(my_month)        # join을 활용해 출력 시 활용할 문자열 생성


  my_day = my_date[6:8]                   # 날짜에서 day에 해당하는 부분만 추출
  my_day_int = int("".join(my_day))       # 값 비교를 위해 int로 변경
  my_day_str = "".join(my_day)            # join을 활용해 출력 시 활용할 문자열 생성

  month_31 = [1,3,5,7,8,10,12]            # 31일까지 있는 month 리스트
  month_30 = [4,6,9,11]                   # 30일까지 있는 month 리스트
  month_28 = [2]                          # 28일까지 있는 month 리스트

  if my_month_int in month_31 and my_day_int <= 31 :
    print(f'#{test_case} {my_year_str}/{my_month_str}/{my_day_str}')
    # month_31에 해당하는 달이면서 day도 31보다 작거나 같을 경우 유효한 날짜

  elif my_month_int in month_30 and my_day_int <= 30 :
    print(f'#{test_case} {my_year_str}/{my_month_str}/{my_day_str}')
    # month_30에 해당하는 달이면서 day도 30보다 작거나 같을 경우 유효한 날짜

  elif my_month_int in month_28 and my_day_int <= 28 :
    print(f'#{test_case} {my_year_str}/{my_month_str}/{my_day_str}')
    # month_28에 해당하는 달이면서 day도 28보다 작거나 같을 경우 유효한 날짜

  else :
    print(f'#{test_case} -1')
    # 위 조건을 만족하지 못할 경우 유효하지 않은 날짜