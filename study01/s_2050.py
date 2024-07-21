# 2050. 알파벳을 숫자로 변환

txt = input()
ans_list = [ord(x)-64 for x in txt] #문자를 아스키코드로 바꾸는 함수 : ord()
# A는 아스키값으로 65이므로, A가 1이 되려면 ord('A')-64 수행

print(*ans_list)