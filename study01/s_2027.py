# 2027. 대각선 출력하기

for i in range(5):
    li = list('+++++') #결과 : ['+','+','+','+','+']
    li[i] = "#"
    #print(*li) #문자 사이에 빈칸 생겨서 안됨
    print("".join(li))