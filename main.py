#!/usr/bin/python
import sys
from app import *
from tests import *
from importer import *

def main():
	if sys.argv[1] == "dev":
		configure_app("dev")
		app.run()
	elif sys.argv[1] == "test":
		test_runner()
	elif sys.argv[1] == "db":
		populate_database()
	else:
		print "Wrong arguments!"
		print "Call \"python main.py dev\" to run the server in developer mode."
		print "Call \"python main.py test\" to run the test cases."
		print "Call \"python main.py db\" to create the database table and populate it with data."

if __name__ == "__main__":
  	main()