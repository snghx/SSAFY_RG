# 1288. 새로운 불면증 치료법 9:02 시작

T = int(input())

for t in range(1, T+1):
    num = int(input())
    num_set = set()
    cnt = 1
    
    while len(num_set) < 10:
        temp = cnt * num
        
        for s in str(temp):
            num_set.add(s)
            
        cnt += 1
    
    print(f"#{t} {temp}")