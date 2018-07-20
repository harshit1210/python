import os
print(os.name)
os.makedirs("khan\demo\class\codes")
print("path created ")
os.rmdir("khan\demo\class\codes")
a=os.path.abspath("E:\python\Analytics-and-Predictive-modeling-for-IPL-cricket-matches")
print(a)
b=os.path.basename("E:\python\Analytics-and-Predictive-modeling-for-IPL-cricket-matches")
print(b)
c=os.path.exists("E:\python\Analytics-and-Predictive-modeling-for-IPL-cricket-matches")
print(c)
d=os.path.join("E:","\python")
print(d)
os.walk("E:\python\Analytics-and-Predictive-modeling-for-IPL-cricket-matches")
for paths,dirs,files in os.walk("."):
	'''for paths in paths:
		print("paths= %s " %paths)'''
	for dirs in dirs:
		print("dirs= %s" %dirs)
	for files in files:	
		print("files = %s" %files)
e=os.path.splitext("E:\python\Analytics-and-Predictive-modeling-for-IPL-cricket-matches\matches.csv")
print(e)
f=os.path.split("E:\python\Analytics-and-Predictive-modeling-for-IPL-cricket-matches")
print(f)
