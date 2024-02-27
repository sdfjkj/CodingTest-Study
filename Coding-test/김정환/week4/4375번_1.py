while True:
    try:
        t = int(input())

        if t == 1:
            print(1)
            break
        n = 1
        n_len = 0

        while (True):
            n_len += 1
            n = n + 10 ** n_len

            if n % t == 0:
                break

        print(n_len + 1)
    except EOFError:
        break