import math

def sum_adj(d, coord):
    s = 0
    for co in [(coord[0]+i,coord[1]+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        s += d.get(co, 0)
    return s

if __name__=="__main__":
    d = {}
    d[(0,0)] = 1
    value = 1
    next_coord = (1, 0)
    n = 1
    while value < 277678:
        d[next_coord] = sum_adj(d, next_coord)
        value = d[next_coord]
        n += 1
        k=math.ceil((math.sqrt(n)-1)/2)
        t=2*k+1
        m=t**2 
        t=t-1
        if n>=m-t:
            next_coord=(k-(m-n),-k)
            continue
        else:
            m=m-t
        if n>=m-t:
            next_coord= (-k,-k+(m-n))
            continue
        else:
            m=m-t
        if n>=m-t:
            next_coord =(-k+(m-n),k)
            continue
        else:
            next_coord= (k,k-(m-n-t))
            continue
    print(value)
