# 2007. 패턴 마디의 길이 (64m)

T = int(input())

for tc in range(1, T+1) :
    text_list = list(map(str, input()))
    check_text = []

    for i in range(1, 11) :
        if text_list[0:i] == text_list[i : 2*i] :
            check_text.extend(text_list[0:i])
            break
    result_len = len(check_text)
    print(f'#{tc} {result_len}')

# for test_case in range(1, T+1) :
#     text = input()
#     text_list = list(map(str,text))
#     new_text_list = []

#     for i in text_list :
#         if i not in new_text_list :
#             new_text_list.append(i)
    
#     text_len = len(new_text_list)

#     print(f'#{test_case} {text_len}')

