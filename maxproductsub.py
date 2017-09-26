#xs=[-2,-3,4,0,-5]
#xs=[2,-3,1,0,-5]
#xs=[2,0,2,2,0]
#xs = [100,-59,1,0,8,-9,12,-87,2]
xs=[10,-2,5,-3,6,-8,2]
def ans(xs):
    r=xs[0]
    maxs = r
    mins = r
    s=len(xs)
    print s
    if s == 1:
        return str(xs[0])
    for i in xs[1:]:
        #print i
        if i<0:
            maxs,mins=mins,maxs
        # if i == 0:
        #    # print "p"
        #     #maxs = r
        #     #mins=0
        #     continue
        # elif i == 1:
        #     continue
        # else:
        maxs = max(i,maxs*i)
           #print maxs,"maxs"
        mins = min(i,mins*i)
        r=max(maxs,r)
    return str(r)
    # try:
    #     if r<10:
    #         return r
    # except ValueError:
    #     print "ss"
print ans(xs)