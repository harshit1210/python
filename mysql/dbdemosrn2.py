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
		# createQuery = "CREATE table IF NOT EXISTS students (rno int(45) AUTO_INCREMENT,name VARCHAR(256) , mobile VARCHAR(45) , PRIMARY KEY (rno))"
		# a = cur.execute(createQuery)

		# insQ = "INSERT INTO `students`(`name`,`mobile`) VALUES (%s , %s)"
		# a = cur.execute(insQ , ("Harshit" , "09876543"))
		# conn.commit()
		# if cur.lastrowid:
			# print("Inserted  Successfully" , cur.lastrowid)
		# else:
		# 	print("there was an error")
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

