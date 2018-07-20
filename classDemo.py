# EMPTY CLASS CREATION
# class Arith:
# 	pass
# a = Arith()

 class nums:
 	# instance variables 
 	a = 10 
 	b = 20
 	c = 300
	# custom constructor 
	def __init__(self):
		print("hello")

	# paramaterised constructor
	def __init__(self , name ):
		print("Hello " + name )



	def add(self,c,d):
	# 	# referencing vars in method using self
		self.c = c
	 	self.d = d
	 	self.sum = self.c+self.d
	 	print(self.sum)
	 	return self.sum 

	# METHOD WITHOUT SELF REFRENCED BY CLASS NAME
	def add(m , n):
	 	print(m+n)
	 	return m+n

	#destructor 
	def __del__(self):
	 	print("object deleted")



ob = nums("khan")
ob.add(10,20) #self = ob
oo = nums("Ravi")
# oo.add(19,13) #self = oo
# print(oo.c)
# #explicit calling of a destructor
# # oo.__del__()

# # CLASS REFERENCED METHOD WITHOUT SELF
# nums.add(20 , 30)

# # object reference
# print("From object 1 " + str(ob.a))
# # class reference
# print("From class " + str(nums.a))
# ob2 = nums()
# ob2.b = 13
# print("From object 2 " + str(ob2.b))
# print("From object 1 " + str(ob.b))
# print("From class " + str(nums.b))
# nums.b = 19
# print("after changing using class")
# print("From object 2 " + str(ob2.b))
# print("From object 1 " + str(ob.b))
# print("From class " + str(nums.b))
# print(type(nums))
# print(type(ob))
# print(type(ob2))
# print(nums)
# print(ob)

class org:
	org_name = "Lync"
	no_of_emps = 20

	def __init__(self , name , mobile):
 		global no_of_emps
 		self.name=name
 		self.mobile=mobile
 		org.no_of_emps=org.no_of_emps + 1
 		print(str(org.no_of_emps) + "  id  of " +name )
	@staticmethod
	def calc(sal , hike):
 		finalAmount = sal * hike
 		print(finalAmount)
 		return finalAmount
	@classmethod
	def change_org(cls , newname):
 		cls.org_name = newname
 		print(cls.org_name)
 		return cls.org_name

o = org("khan" , "9876543210")
o.calc(12000 , 0.05)
m = org("ravi" , "9876543210")
print(o.org_name)
org.change_org("DigitalLync")
print(org.org_name)
print(o.org_name)
o.change_org('motors')
org.change_org('cars')  #object refernce is not keeping the varible value same from class refe
print(o.org_name)
print(m.org_name)
print(org.org_name)





