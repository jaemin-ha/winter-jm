T = int(input())

for tc in range(1, T+1):
    K = int(input())
    string = input()

    lst = []

    new_string = string[::-1]

    for i in range(len(new_string)):
        lst.append(new_string[:i+1][::-1])

    lst.sort()
    if K-1 >= len(lst):
        print(f'#{tc} none')
    else:
        print(f'#{tc} {lst[K-1]}')