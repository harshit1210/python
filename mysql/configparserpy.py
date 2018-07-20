#configparserpy.py
# this configparser will parse my config.ini to get credentials
from configparser import ConfigParser
# filename , section
def getcreds(file = "dbconfig.ini" , section = "mysql"):
	dbdict = {}
	# make a parser object
	parser = ConfigParser()
	# read file using parser object
	parser.read(file)

	if parser.has_section(section):
		items = parser.items(section)
		# print(items)
		for item in items:
			# print(item)
			dbdict[item[0]] = item[1]
	# print(dbdict)
	return dbdict

getcreds()


