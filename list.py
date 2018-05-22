tech=["py","cpp","java","c","php","css","html",".net"]
int=[1,2,5]
res=[]
result=[]
for i in range(0,len(int)):
	res.append(tech[int[i]])
print(res)	
for j in range(0,len(tech)):
	if(tech[j] not in res):
		result.append(tech[j])
print(result)



lnum=[1,2,3,4,5,6,7,8,9,20]
square=[]
for i in range(0,len(lnum)):
	mid=lnum[i]**2
	square.append(mid)
print(square)