#class
class company:
	company_nm="organizatn1"
	no_of_emps=40
	newemp=[]
	def __init__(self,name,mobile):
		self.name=name
		self.mobile=mobile       #no_of emps not accesseable even after using global
		company.no_of_emps=company.no_of_emps+1
		company.newemp.append(self.name)
		print(company.newemp)

	def id(self,name):
		self.id_new=company.no_of_emps
		print(str(self.id_new)+'id of ' + name)
	@classmethod
	def company_hike(cls,salary,hike):
		cls.newsalary=salary*hike+salary
		print(cls.newsalary)
	def performance_hike(self,name,hike,salary):
		self.new_salary=salary*hike+salary
		print(self.new_salary)
	#	print(self.newsalary)  #here it is takeing variable value from method
		#return self.newsalary
	#def salary(self):
	def __str__(self):
		return "(%s, %d)" %(self.name, self.mobile)
	#print(str(self.mobile))
	def remove(self,name):
		company.newemp.remove(self.name)
		company.no_of_emps=company.no_of_emps-1
		print(company.no_of_emps)
	#def __del__(self):	#is automatically called at end so no need to call
		#print(company.newemp)
		#company.newemp.remove('khan')
		#print('object deleted')
		#company.newemp.remove(self.name)
new1=company('khan',7792345)
#how to acesss id
new1.id('khan')
new1.company_hike(12000,.1)	
company.company_hike(120000,.1)
new1.performance_hike('khan',.1,200)
print(new1)#str returned non string type error(we can't use print in str insted use return as above)
new2=company('hari',455665)
new3=company('ram',839494)
new1.remove('khan')
print(company.newemp)

