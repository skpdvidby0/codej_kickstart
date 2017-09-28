def answer(xs):
    # your code here
    posnos = [x for x in xs if x > 0]
    negnos = [x for x in xs if x < 0]
    r = 1
    posl = len(posnos)
    negl = len(negnos)
    if (posl == 0 and negl == 0) or (posl == 0 and negl == 1):
        return xs[0]

    elif posl == 0:
        if negl % 2 == 0:
            negnos.remove(max(negnos))
            negl = negl - 1
        for i in negnos:
            r = r * i
        return r

    elif negl == 0 or negl == 1:
        for i in posnos:
            r = r * i
        return r

    else:
        if negl % 2 == 0:
            negnos == negnos.remove(max(negnos))
            negl = negl - 1
        for i in negnos:
            r = r * i

        for i in posnos:
            r = r * i
        return r

print answer(xs)