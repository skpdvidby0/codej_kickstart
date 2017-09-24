def ans(n):
    i=1
    count=1
    #print count
    while i*i<n:
        i = i + 1
        if i*i>n:
            i=i-1
            break

    c=n-(i*i)
    #print c
    if c==0:
        return count
    elif c>1:
        return count + ans(c)
    elif c==1:
        return count+1

    else:
        return 1
t=int(raw_input())
for i in xrange(1,t+1):
    n=int(raw_input())
    print "Case #{}: {}".format(i, int(ans(n)))
   # print ans(n)

# for i in xrange(1,t+1):
#     n=int(input())
#     print ans(n)



#print ans(34)