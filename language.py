def lanuage(y):
    t = 0 
    T = 0 
    s = 0 
    S = 0 
    for i in range(len(y)):
        if y[i] == "t":
            t = t +1
        if y[i] == "T":
            T = T + 1
        if y[i] == "s":
            s = s + 1
        if y[i] == "S": 
            S = S + 1
    print(t,T,s,S)
    if t + T > s + S:
        print("english")

    if t + T < s + S:
        print("probably french")


lanuage("sssTTTTTTTT")