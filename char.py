#print_abc
import sys
a=int(sys.argv[1])
for i in range(0,a):
	output=chr(97+i)
	print(output,end="")


#print_random_abc
import random as r
b=[j for j in range(65,123)]
c=int(sys.argv[2])
for k in range(0,c):
	output2=chr(r.choice(b))
	print(output2,end="")

