# 펠린드롬 수 찾기
# 펠린드롬수: 1221처럼 거꾸로 읽어도 같은 수

def check_palindrome(word):
    trial = len(word)//2

    for i in range(trial):
        if word[i] != word[-(i+1)]:
            return False
    return True

while True:
    word = input()
    if word == '0' : exit(0)

    if check_palindrome(word): print('yes')
    else: print('no')