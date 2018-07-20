#authentication_using_file
import random as r
def usrChk(name):
	with open('pwd.txt','r') as fobj:
		a=fobj.read()
	b=a.split()
	if name in b :
		return 0
	else:
		return 1 
def numPwd(n):
	numpass = ""
	for i in range(1 , n+1):
		numpass = numpass+str(r.randint(0,9))
	# print(numpass)
	return numpass

def chrPwd(n):
	chrpwd = ""
	chrslist = []
	for i in range(1 , (n//2)+1):
		chrslist.append(chr(r.randint(65 , 90)))
		chrslist.append(chr(r.randint(97 , 122)))
		# r.sample(chrslist , k = 4)
	for i in r.sample(chrslist , k = n):
		chrpwd = chrpwd + i
		# chrpwd = chrpwd + chr(c) + chr(l)
	# print(chrpwd)
	return chrpwd
# chrPwd(4)
# numPwd(4)


def genPwd(name):
	if usrChk(name) == 1:
		password = numPwd(8)+chrPwd(2)+numPwd(2)+chrPwd(4)
		print(" %s -- %s%s%s%s"  %(name , numPwd(8),  chrPwd(2), numPwd(2), chrPwd(4)))
		writeonfile(name ,password )
		return password
	else:
		print("already exist")
def writeonfile(name , pwd):
	mypwd = name + " - " + pwd + "\n"
	with open("pwd.txt" , "a") as fw:
		fw.write(mypwd)

name=input(str("enter the name:"))
genPwd(name)