list1=["name","age","gender","qualification"]
list2=["david",28,"male","B.com"]
dict={}
for i in range(0,len(list1)):
	dict[list1[i]]=list2[i]
print(dict)
dict.item()