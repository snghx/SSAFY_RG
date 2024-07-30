# 1945. 간단한 소인수분해

T = int(input())

for test_case in range(1, T+1):

    num = int(input())

    a,b,c,d,e = 0,0,0,0,0

    while num != 1 :
          if num % 2 == 0 :
                a+=1
                num = num / 2
          if num % 3 == 0 :
                b+=1
                num = num /3
          if num % 5 == 0 :
                c+=1
                num = num / 5
          if num % 7 == 0 :
                d+=1
                num = num / 7
          if num % 11 == 0 :
                e+=1
                num = num / 11
        
    print(f'#{test_case} {a} {b} {c} {d} {e}')






    