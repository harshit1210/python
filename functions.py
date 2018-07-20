#dfault_parameter1
'''def make_cake(flav='vani',weigh=2,shape='round'):
	print("you have ordered",flav,"flavoured cake of",weigh,"kg",shape, "shaped")

make_cake("vani",4,"square")

#default_parameters2
def make_cake(flav='vani',shape='round',weigh=2):
	print("you have ordered",flav,"flavoured cake of",weigh,"kg",shape, "shaped")

make_cake( "square",4)

#default_parameter_3
def make_cake(flav='vani',shape='round',weigh=2):
	print("you have ordered",flav,"flavoured cake of",weigh,"kg",shape, "shaped")

make_cake( shape="square",weigh=4)



def add(*args):
	#it_adds
	print(*args)
	sum=0
	for i in args:
		sum=sum+i
	print(sum)
add()
add(1,2)
add(1,2,3)


def avg(a,b,*args):
	sum=a+b
	count=0
	for i in args:
		sum=sum+i
		count+=1
	avg=sum/(count+2)
	print(avg)


avg(1,2,3,4,5,6)
def power(a, b):
    """Returns arg1 raised to power arg2."""
  
    return a**b
 
print(add.__doc__)'''


def operation():
	"""	 1.median
		2.mean
		3.largest no."""
	print(operation.__doc__)
	a=int(input('enter an option'))
	if(a==1):
		median()
	elif(a==2):
		mean()
	elif(a==3):
		largest_no()
	else:
		print('wrong input')


def mean():
	a=int(input("no. of input:" ))
	sum=0
	for i in range(0,a) :
		b=int(input("enter the input:"))
		sum=sum+b
	avg=sum/a
	print(avg)


def median():
	a=int(input("no. of input:" ))
	list=[]
	for i in range(0,a) :
		b=int(input("enter the input:"))
		list.append(b)
	list.sort()
	print(list)
	if(a%2!=0):
		m=(a+1)
		v=m//2
		print(list[v-1])
	else:
		n=a//2
		t=list[n]
		j=list[n-1]
		d=(t+j)/2
		print(t)
		print(j)
		print(d)	


def largest_no():
	a=int(input("no. of input:" ))
	list=[]
	for i in range(0,a) :
		b=int(input("enter the input:"))
		list.append(b)
	list.sort()
	for i in list:
		count=0
		for j in list:
			if(i>=j):	
				count+=1
			else: 
				pass
		if(count==a):
				answer=i
	print(answer)

operation()



