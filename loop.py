
"""for i in range(10) :
	print (i)



for i in range(2,10):
	print(i)
	
 

for i in range(10,2,-1):
	print(i) 




#primeandcomposite
n=12
count=0
for i in range(1,n+1):
	if(n%i==0):
		count+=1
		print(i,end="")
print()
if(count>2):
	print(n,"composite")
else:
    print(n,"prime")



#primeandcompositbetween3-100
for i in range(3,100):
	count=0
	for j in range(1,i+1):
		if(i%j==0):
			count+=1
			print(j)
	if(count>2):
		print(i,"composite")
	else:
		print(i,"prime")"""

"""



#printabcinpattern
count=0
for i in range(97,102):
	new=97
	for j in range(count+1):
		print(chr(new),end="")
		new+=1
	count+=1
	print()"""





#if3and5arefactors
#
"""import sys
num=int(sys.argv[1])
if(num%5==0 and num%3!=0):
	print("only5")
elif(num%3==0 and num%5!=0):
	print("only 3")
elif(num%3==0 and num%5==0):
	print("3 and 5")
else:
	print("nothing")
print(sys.argv[2])
"""


#useofbreak
"""i=1
while(i<=10):
	if(i==5):
		break
	else:
		print(i)
		i+=1"""




i=0
while(i<=10):
	if(i==5):
		i+=1
		continue
		
else:
	print(i)
	i+=1
	