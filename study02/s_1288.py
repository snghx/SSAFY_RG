# 1288. 새로운 불면증 치료법

T = int(input())

for t in range(1, T+1):
    num = int(input())
    num_set = {}
    cnt = 1
    
    while len(num_set) != 10:
        for n in str(num):
            print(n)
            num_set.update(n)
            
        print(num_set)
        num = int(num) * cnt
        cnt += 1
    
    print(f"#{t} {cnt}")