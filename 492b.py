n,l = raw_input().split()
n = int(n)
l = int(l)
lamps_pos = map(int,raw_input().split())
lamps_pos.sort()
d=0


start = lamps_pos[0]
end = lamps_pos[len(lamps_pos)-1]

def min_distance(lamps_pos,radius):
    d = 0
    for i in range(1,len(lamps_pos)):
        d1 = (lamps_pos[i] - lamps_pos[i-1])/float(2)
        d = max(d1,radius,d)
    return d

if start == end:
    d = max(start , l-end)
else:
    if start != 0 and end != l:
        radius = max(start,(l-end))
        d = min_distance(lamps_pos,radius)

    else:
        if start == 0 and end!=l or start!=0 and end == l:
            if start == 0 :
                radius = (l-end)
            if end == l:
                radius =  start
            d = min_distance(lamps_pos,radius)
        else:
            radius = 0
            d = min_distance(lamps_pos,radius)

print d
