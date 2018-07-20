import pymysql
from configparserpy import getcreds
try:
	# conn = pymysql.connect(host="localhost" , user = "root" , password="khan" , database = "demodb")
	dbdetails = getcreds()
	conn = pymysql.connect(**dbdetails)
	if conn:
		print("connection made successfully")

except Exception as e:
	print(e)

finally:
	conn.close()
	print("connection has been closed ")

