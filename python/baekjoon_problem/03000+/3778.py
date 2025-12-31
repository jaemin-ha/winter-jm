# 백준 3778 애너그램 거리

# 처음 : 그냥 더 해서 짝수의 종류를 세자 -> "ppaa", "bbcc" : 예외
# 2번째 : 빼자 -> "aaa", "b" : 답은 4지만, 코드론 2가 나와서 안됨
# 결론 : 리스트 돌면서 절댓값을 더하는 방식

N = int(input())

for tc in range(1, N+1):
    word_1 = input()
    word_2 = input()

    lst = [0] * 26

    for i in range(len(word_1)):
        lst[ord(word_1[i]) - 97] += 1

    for i in range(len(word_2)):
        lst[ord(word_2[i]) - 97] -= 1

    # 애너그램 거리
    cnt = 0

    # 0이 아닌 것들의 숫자를 다 더해야 함
    for i in range(len(lst)):
        if lst[i]:
            cnt += abs(lst[i])

    # 출력
    print(f"Case #{tc}: {cnt}")