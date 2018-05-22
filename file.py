def position(f_object):
	f_object.seek()
import sys
l1=[]
f_object=open('demo.txt','w+')
for i in range(90):
	f_object.write(str(i))
f_object.close()
c=int(sys.argv[1])
f_object2=open('demo.txt','r')
position(f_object2)
a=f_object2.read(c)
print(a)
g=f_object2.tell()
l1.append(g)
f_object2.close()



