temple='{:d}*{:d}={:2d}'
for x in range(10):
    temple2=''
    temple1=''
    for y in range(x):
        res=(x)*(y+1)
        temple2=temple.format(y+1,x,res)
        temple1=temple1+temple2+' '*(7-len(temple2))
    print(temple1)