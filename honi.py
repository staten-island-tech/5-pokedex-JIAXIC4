

def hon(x):
    honi = 1
    honip= 0        
    for i in x:
        if honi == 1 and i == "H":
            honi = honi +1
        if honi == 2 and i == "O":
            honi = honi +1
        if honi == 3 and i == "N":
            honi = honi+1
        if honi == 4 and i == "I":
            honip= honip +1
            
    print(honip)

hon("HONIHOOOOOOOOONI")