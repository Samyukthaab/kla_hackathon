with open('Testcase1.txt') as f:
    lines = f.readlines()

print(lines)
d = lines[0]
diameter = eval(d[14:])
#print(diameter)
s=lines[1]
diesize = [eval(s[8:10]),eval(s[11:13])]
#print(diesize)
v=lines[2]
shift = [eval(v[16]),eval(v[18])]
#print(shift)
r=lines[3]
ref = [eval(r[14:16]),eval(r[17:19])]
#print(ref)

length=diesize[0]
height = diesize[1]
radius=diameter//2

llcx=ref[0]-length//2
llcy=ref[1]-height//2
x=0
y=0
ans=[]


#ans.append([(x,y),(llcx,llcy)])

while(llcy<radius):
    ans.append([(x,y),(llcx,llcy)])
    rightx=llcx+length
    while(rightx<radius):
        x+=1
        if ((rightx*rightx)+(llcy*llcy))<=(radius*radius):
            ans.append([(x,y),(rightx,llcy)])
        rightx+=length

    x=0
    rightx=llcx-length
    while(rightx>=(-radius) or (rightx+length)>(-radius)):
        x-=1
        if ((rightx*rightx)+(llcy*llcy))<=(radius*radius):
            ans.append([(x,y),(rightx,llcy)])
        rightx-=length
    
    llcy+=length
    y+=1
    x=0

llcx=ref[0]-length//2
llcy=ref[1]-height//2
x=0
y=-1
llcy-=height
while((llcy>=(-radius)) or (llcy+length>(-radius))):
    ans.append([(x,y),(llcx,llcy)])
    rightx=llcx+length
    while(rightx<radius):
        x+=1
        if ((rightx*rightx)+(llcy*llcy))<=(radius*radius):
            ans.append([(x,y),(rightx,llcy)])
        rightx+=length
    
    if (llcy+length>(-radius)):
        while(rightx<radius):
            x+=1
            l=llcy+length
            if ((rightx*rightx)+(l*l))<=(radius*radius):
                ans.append([(x,y),(rightx,llcy)])
            rightx+=length

    x=0
    rightx=llcx-length
    while(rightx>=(-radius) or (rightx+length)>(-radius)):
        x-=1
        if ((rightx*rightx)+(llcy*llcy))<=(radius*radius):
            ans.append([(x,y),(rightx,llcy)])
        rightx-=length

    
    llcy-=length
    y-=1
    x=0


print(len(ans))
print(ans)


file1 = open('output1.txt','w')
for i in ans:
    file1.write('(')
    file1.write(','.join(str(s) for s in i[0]))
    file1.write(')')
    file1.write(":")
    file1.write('(')
    file1.write(','.join(str(s) for s in i[1]))
    file1.write(')\n')
file1.close()



