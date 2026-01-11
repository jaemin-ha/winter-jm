# 백준 1673 치킨 쿠폰
# 입력만 들어오는 경우 까먹어서 검색함

while True:
    try:
        n, k = map(int, input().split())

        chicken = n
        stamp = n

        while True:
            # 쿠폰을 사용가능하면
            if stamp >= k:
                use = stamp // k
                chicken += use
                stamp += use
                stamp -= use * k

            # 적으면 종료
            if stamp < k:
                break

        print(chicken)

    except EOFError:
        break