import pymysql
from configparserpy import getcreds

try:
	# conn = pymysql.connect(host="localhost" , user = "root" , password="khan" , database = "demodb")
	dbdetails = getcreds()
	# establishing a connection
	conn = pymysql.connect(**dbdetails)
	if conn:
		print("connection made successfully")
		# making a cursor object
		cur = conn.cursor()
		createQuery = "CREATE table IF NOT EXISTS registration (id int(45) AUTO_INCREMENT,name VARCHAR(256) , email VARCHAR(45) , PRIMARY KEY (id))"
		a = cur.execute(createQuery)
		def insq(registrations):
			dict={'name':['harshit','ravi','khan'],'email':['abc','xyz','pqr']}
			for i in dict.keys():
				"INSERT INTO registration ('i') VALUES(dict[i])" 
			return registration
		insq1=insq('registration')
		#insQ = "INSERT INTO `students`(`name`,`mobile`) VALUES (%s , %s)"
		a = cur.execute(insq1)
		conn.commit()
		if cur.lastrowid:
			 print("Inserted  Successfully" , cur.lastrowid)
		else:
		 	print("there was an error")
		selQ = "select * from students"
		cur.execute(selQ)
		rows = cur.fetchall()
		for row in rows:
			print(row)
except Exception as e:
	print(e)

finally:
	conn.close()
	print("connection has been closed ")

