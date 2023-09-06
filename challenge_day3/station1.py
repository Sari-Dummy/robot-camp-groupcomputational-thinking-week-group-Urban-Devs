def solution_station_1(position):
    if position <= 0:
        return 0
    elif position == 1:
        return 1
    else:
        fib = [0] * (position + 1)
        fib[1] = 1
        for i in range(2, position + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        print(fib[position])
        return fib[position]



