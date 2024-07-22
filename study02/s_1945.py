# 1945. 간단한 소인수분해

T = int(input())

for t in range(1, T+1):
    num = int(input())
    nums = [2, 3, 5, 7, 11]
    ans_list = [0, 0, 0, 0, 0]
    
    for i in range(5):
        while num%nums[i] == 0:
            ans_list[i] += 1
            num = num/nums[i]
    print(f"#{t}", *ans_list)