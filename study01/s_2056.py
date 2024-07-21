# 2056. 연월일 달력

T = int(input())
end_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #각 달의 마지막 날짜 저장

for t in range(1, T+1):
    days = input() #슬라이싱 해야 하므로, int가 아닌 str형(default)으로 저장
    
    #년/월/일 각각 저장
    y = days[0:4]
    m = days[4:6]
    d = days[6:8]
    
    if 0 < int(m) < 13:
        if int(d) <= end_day[int(m)-1]: #input으로 들어온 값이, 해당 달의 마지막 날과 같거나 작다면 (포함된다면)
            print(f"#{t} {y}/{m}/{d}") #날짜 형식대로 출력
        else:
            print(f"#{t} -1")
    else:
        print(f"#{t} -1")