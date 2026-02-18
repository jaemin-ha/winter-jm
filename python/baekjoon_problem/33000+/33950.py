# 백준 33950 어게인 포닉스

N = int(input())

for _ in range(N):
    word = input()
    # replace 했을 시 새로운 변수로 선언 후 출력
    new_word = word.replace("PO", "PHO")

    print(new_word)