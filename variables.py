#findletterinstring
"""l=["digital","lync","gachibowli","kukatpally"]
a="lync"
b=a in l
print(b)"""
 


#bitwiseoperators
"""c=45
d=65
not1=~c
print(not1)
not2=~d
print(not2)
xor1=c^d
print(xor1)
rs1=c>>2
print(rs1)
rs2=d>>2
print(rs2)
ls1=c<<2
print(ls1)
ls2=d<<2
print(ls2)"""


#operationofnumbers
"""z=100.00
import cmath
t=complex(z)
print(t)
factorial=1
q=int(z)
print(q)
for i in range(1,q+1):
	factorial=i*factorial
print(factorial)
import math
sq=math.sqrt(z)
print(sq)
exponent=z**2
print(exponent)"""


#sumofdigits
"""
a="6418999"
d=len(a)
sum=0
for i in range(0,d):
		t=int(a[i])
		sum=sum+t
print(sum)

"""




#comparison

a=15
b=2
if(a==b):
	print("a=b")
else:
	print("a is not equal b")
if(a>=b):
	print("a is greater than or equal to b")
else:
	print("a is less than or equal to b")
if(a>>b):
	print("a is greater than b")
else :
	print("a is less than b")