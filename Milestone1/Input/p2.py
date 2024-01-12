import math

with open('Testcase2.txt') as f:
    lines = f.readlines()
d = lines[0]
diameter = eval(d[14:])
#print(diameter)
p=lines[1]
points = eval(p[15:])
#print(points)
a=lines[2]
angle = eval(a[6:])
print(angle)

radian = angle * math.pi / 180
#radian = angle

#diameter line (x- axis)
radius = diameter/2

x1 = -(radius*math.cos(radian))
y1 = -(radius*math.sin(radian))
x2 = (radius*math.cos(radian))
y2 = (radius*math.sin(radian))

x1=round(x1,4)
x2=round(x2,4)
y1=round(y1,4)
y2=round(y2,4)

print(x1,y1)
print(x2,y2)

c=[]
if (x1-int(x1))==0.0:
    x1=int(x1)
c.append((x1,y1))

gap = diameter/(points-1)
print('g',gap)

i=1
points-=2
while(i<=points):
    x1+=(gap*math.cos(radian))
    y1+=(gap*math.sin(radian))
    x1=round(x1,4)
    y1=round(y1,4)
    if (x1-int(x1))==0.0:
        x1=int(x1)
    if (y1-int(y1))==0.0:
        y1=int(y1)
    c.append((x1,y1))
    i+=1


if (x2-int(x2))==0.0:
    x2=int(x2)
c.append((x2,y2))

print(len(c))
print(c)

file1 = open('output2.txt','w')
for i in c:
    file1.write('(')
    file1.write(','.join(str(s) for s in i))
    file1.write(')\n')
file1.close()