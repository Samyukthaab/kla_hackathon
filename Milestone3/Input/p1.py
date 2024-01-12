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

number=[2,2]
diestreet=[5,5]
reticlestreet=[10,10]

x=0
y=0
radius = diameter//2

llcx=0
llcy=0
length = 30
height = 30
rwidth=10
dwidth=5
rheight=10
dheight=5

ans=[]

c=1
while(llcy<radius):
    ans.append([(x,y),(llcx,llcy)])
    rightx=llcx+length
    rightx+=dwidth
    while(rightx<radius):
        x+=1
        c+=1
        if ((rightx*rightx)+(llcy*llcy))<=(radius*radius):
            ans.append([(x,y),(rightx,llcy)])
        if c%2==0:
            rightx+=rwidth
        rightx+=length
    break

'''
    x=0
    rightx=llcx-length
    rightx-=dwidth
    while(rightx>=(-radius) or (rightx+length)>(-radius)):
        x-=1
        c+=1
        if ((rightx*rightx)+(llcy*llcy))<=(radius*radius):
            ans.append([(x,y),(rightx,llcy)])
        if c%2==0:
            rightx-=rwidth
        rightx-=length
    
    llcy+=length
    y+=1
    x=0
    break
'''

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