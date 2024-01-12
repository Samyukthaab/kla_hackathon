with open('Testcase1.txt') as f:
    lines = f.readlines()
d = lines[0]
diameter = eval(d[14:])
#print(diameter)
p=lines[1]
points = eval(p[15:])
#print(points)
a=lines[2]
angle = eval(a[6:])
#print(angle)

#diameter line (x- axis)
radius = diameter/2
x1=round(-radius,1)
y1=0
x2=round(radius,1)
y2=0

c=[]
points-=2
if (x1-int(x1))==0.0:
    x1=int(x1)
c.append((x1,y1))

gap = diameter/(points-1)
gap=round(gap,1)
print('g',gap)

i=0
while(x1<=x2 and i<=points):
    x1+=gap
    x1=round(x1,1)
    if (x1-int(x1))==0.0:
        x1=int(x1)
    c.append((x1,y1))
    i+=1

if (x2-int(x2))==0.0:
    x2=int(x2)
c.append((x2,y2))




#number of points to be placed


#x1 = round(x1,1)
#if (x1-int(x1))==0.0:
#    x1=int(x1)
#c.append((x1,y1))


print(len(c))
print(c)

file1 = open('output1.txt','w')
for i in c:
    file1.write('(')
    file1.write(','.join(str(s) for s in i))
    file1.write(')\n')
file1.close()