def solution_station_4(number):
    # thanks stackoverflow
    state = True
    if number <= 0:
        state = False
        print(state)
        return state
    else:          
        for i in range(2,number):
            if number % i == 0:
                state = False
                break
        print(state)
        return state
