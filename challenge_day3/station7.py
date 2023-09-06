def solution_station_7(equation):
    a = 3
    b = -1
    c = 4
    d = 7
    e = 0.5
    result = 0
    operator = "add" 
    for char in equation: 
        if char == "a":
            if operator == "add":
                result += a
            if operator == "mult":
                result *= a
        if char == "b":
            if operator == "add":
                result += b
            if operator == "mult":
                result *= b
        if char == "c":
            if operator == "add":
                result += c
            if operator == "mult":
                result *= c
        if char == "d":
            if operator == "add":
                result += d
            if operator == "mult":
                result *= d
        if char == "e":
            if operator == "add":
                result += e
            if operator == "mult":
                result *= e
        if char == "+":
            operator = "add"
        if char == "*":
            operator = "mult"

    print(result)
    return result


