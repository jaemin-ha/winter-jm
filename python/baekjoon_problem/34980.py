# 백준 34980 생수병 놓기

N = int(input())

s = input()
e = input()

if s == e:
    print("Good")

else:
    if s.count("w") == e.count("w"):
        print("Its fine")

    elif s.count("w") > e.count("w"):
        print("Oryang")

    else:
        print("Manners maketh man")