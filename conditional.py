#conditional
#1
"""import sys
marks=int(sys.argv[1])
if(marks>50 and marks<55):
	print("second class")
elif(marks>55 and marks<60):
	print("higher second class")
elif(marks>60 and marks<65):
	print("first class")
elif(marks>65):
	print("distinction")
else:
	print("pass")

"""

#2
"""import sys
year=int(sys.argv[1])
if(year%4==0 and year%100==0 and year%400==0 ):
	print("leap year")
elif(year%4==0 and year%100!=0):
	print("leap year")
else:
	print("not a leap year")"""

#3
"""import sys
number=int(sys.argv[1])
if(number%2==0):
	print("even number")
else:
	print("odd number")"""


#5
import sys
number1=int(sys.argv[1])
number2=int(sys.argv[2])
number3=int(sys.argv[3])
if(number1>number2 and number1>number3):
	print("%d is the greatest" %(number1))
elif(number2>number1 and number2>number3):
	print("%d is the greatest number" %(number2))
else:
	print("%d is the greatest number"%(number3))
