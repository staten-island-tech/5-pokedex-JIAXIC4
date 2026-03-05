def testcheck(n,q,a):
    rect = 0

    for x in range(len(q)):
        if q[x] == a[x]:
            rect = rect + 1


    print(rect)

testcheck(3,"ABC","CBA")