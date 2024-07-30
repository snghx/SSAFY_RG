# 1940. 주몽

n = int(input())
m = int(input())

my_list = list(map(int, input().split()))
my_list.sort()

i = 0          # start_index
j = n-1        # end_index

cnt = 0

while i < j: 
    if my_list[i] + my_list[j] < m :
        # 두 재료의 합이 갑옷을 만들 때 필요한 수보다 작다면
        i += 1
        # start_index를 한 칸 뒤로 이동한다
    elif my_list[i] + my_list[j] > m :
        # 두 재료의 합이 갑옷을 만들 때 필요한 수보다 크다면
        j -= 1
        # end_index를 한 칸 앞으로 이동한다
    else : 
        # 두 재료의 합이 갑옷을 만들 때 필요한 수와 같다면
        cnt += 1
        # 경우의 수에 1을 더한다
        i+=1
        # start_index를 한 칸 뒤로 이동한다
        j-=1
        # end_index를 한 칸 앞으로 이동한다

print(cnt)