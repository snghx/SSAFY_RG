# 1926. 간단한 369 게임 (45m)

N = int(input())

game_list = []

for i in range(1, N+1) :
    num = str(i)
    num = num.replace('3','-') # 3을 -로 바꾸기
    num = num.replace('6','-') # 6을 -로 바꾸기
    num = num.replace('9','-') # 9를 -로 바꾸기
    game_list.append(num) # 숫자가 모두 들어있는 리스트 생성

# 13 -> '1-' / 37 -> '-7'과 같은 경우가 발생하기에 새로운 리스트에 해결하여 저장
game_list2 = []

for n in game_list :
    if '--' in n :
        game_list2.append('--')
    elif '-' in n :
        game_list2.append('-')
    else :
        game_list2.append(n)

print(*game_list2)
