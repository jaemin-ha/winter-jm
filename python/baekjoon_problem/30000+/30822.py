# 백준 30822 UOSPC 세기

N = int(input())
string = input()

lst = [0] * 26
search = ["u", "o", "s", "p", "c"]

for alphabet in string:
    if alphabet in search:
        lst[ord(str(alphabet))-97] += 1

new_lst = [lst[2], lst[14], lst[15], lst[18], lst[20]]
print(min(new_lst))