import ftplib
from ConfigParser import SafeConfigParser
import argparse
import sys
import os



def upload(filename):

	parser = SafeConfigParser()
	parser.read('config.ini')
	
	host  = parser.get('FTP Server','host')
	user = parser.get('FTP Server','user')
	password = parser.get('FTP Server','pass')
	
	session = ftplib.FTP(host,user,password)
	filename_extension_together = os.path.splitext(filename)
	storefilename = filename_extension_together[0]+filename_extension_together[1]
	file = open(filename,'rb')                  # file to send
	print "Sending ..."
	session.storbinary('STOR '+storefilename, file)     # send the file
	print "Uploaded File ..."
	file.close()                                    # close file and FTP
	print "Operation Done Session Closed ..."
	session.quit()




if __name__ == "__main__":
	
	  
	
	  if len(sys.argv) == 1:
	  	 print "usage : ./uploadFtp -file [PATH] / --help"
	  	 exit(0)
	  
	  elif len(sys.argv) == 2: 
	  	 if  sys.argv[1] == '--help':
	  	 	print "usage : ./uploadFtp -file [PATH] / --help"
	  	 	exit(0)
	  	 else :
	  	 	print "Not correct Usage: Please Type --help option"
	  	 	exit(0)
	  	 	
	  elif len(sys.argv) == 3 :
	  		if sys.argv[1] == '--help':
	  			print "usage : ./uploadFtp -file [PATH]"
	  	 		exit(0)
	  		elif sys.argv[1] == '--file':
	  			upload(sys.argv[2])
	  			exit(0)
	  		else:
	  			print "Not correct Usage: Please Type --help option"
	  	 		exit(0)	
	  else:
	  	print "too many parameters not correct usage : --help option"
	  	exit(0)
	  	 	
