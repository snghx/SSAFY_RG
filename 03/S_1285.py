# 1285. 아름이의 돌 던지기 (13m)

T = int(input())

for tc in range(1,T+1) :
    n = int(input())
    score_list = list(map(int, input().split()))
    score_list_abs = [] 

    for score in score_list :
        score = abs(0 - score) 
        score_list_abs.append(score)
    
    best_score = min(score_list_abs)

    people = 0
    for n in score_list_abs :
        if n == best_score :
            people += 1
    
    print(f'#{tc} {best_score} {people}')