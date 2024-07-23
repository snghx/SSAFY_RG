# 1936. 1대1 가위바위보

a, b = map(int, input().split())

def my_rcp_game(a, b) :
  if a == 1 and b == 2 :
    return 'B'
  if a == 1 and b == 3 :
    return 'A'
  if a == 2 and b == 1 :
    return 'A'
  if a == 2 and b == 3 :
    return 'B'
  if a == 3 and b == 1 :
    return 'B'
  if a == 3 and b == 2 :
    return 'A'

print(my_rcp_game(a,b))