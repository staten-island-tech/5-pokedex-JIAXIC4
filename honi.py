h = False
o = False
n = False
i = False

def honi (x):
    honi = 0
    for i in range (len(x)):
        if x[i] == "h" or x[i] == "H":
            h = True

        elif h == True:
            if x[i] == "o" or x[i] == "O":
                o == True
                
        elif o == True:
            if x[i] == "n" or x[i] == "N":
                n == True

        elif n == True:
            if x[i] == "i" or x[i] == "I":
                h = False
                o = False
                n = False
                honi = honi + 1
    print(honi)

honi("HONI")

