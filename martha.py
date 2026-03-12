def martha_gamble(x):
    total_time= 0
    first = 0
    second = 0
    third = 0
    position = 0
    money = 0

    while position == 0:
        first += 1
        money = money - 1
        total_time += 1 
        position = position +1
        if first == 35:
            money = money + 30
            first = 0 

        if position == 1:
            second += 1
            money = money - 1
            total_time += 1 
            position = position +1
            if second == 100:
                money = money + 60
                second = 0 

        if position == 2:
            third += 1
            money = money - 1
            total_time += 1 
            position = position +1
            if third == 10:
                money = money + 9
                third = 0 
    if money == 0:
        print("Martha plays", total_time)

    print(total_time)
        
martha_gamble(1005)