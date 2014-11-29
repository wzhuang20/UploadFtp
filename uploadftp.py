import ftplib
from ConfigParser import SafeConfigParser
import argparse
import sys
import os



def upload(filename,filedirectory = None,folderstate = 0):

	parser = SafeConfigParser()
	parser.read('config.ini')
	
	host  = parser.get('FTP Server','host')
	user = parser.get('FTP Server','user')
	password = parser.get('FTP Server','pass')
	
	session = ftplib.FTP(host,user,password)
	filename_extension_together = os.path.splitext(filename)
	storefilename = filename_extension_together[0]+filename_extension_together[1]
	file = open(filename,'rb')                  # file to send
	print "Opening Folder %s " ,filedirectory
	print "Sending ..."
	


	if folderstate == 1 : # setting folder name
		session.cwd(filedirectory)

	elif folderstate == 2: #new folder create command
		session.mkd(filedirectory)
	 	session.cwd(filedirectory)
	
 	

	session.storbinary('STOR '+storefilename, file)     # send the file
	print "Uploaded File ..."
	file.close()                                    # close file and FTP
	print "Operation Done Session Closed ..."
	session.quit()



def getList(filedirectory = None):
	parser = SafeConfigParser()
	parser.read('config.ini')
	
	host  = parser.get('FTP Server','host')
	user = parser.get('FTP Server','user')
	password = parser.get('FTP Server','pass')
	
	session = ftplib.FTP(host,user,password)
	filelist = [] #to store all files
	if filedirectory is not None: # current directory list
		session.cwd(filedirectory)               # change into "debian" directory
	print "List of Content"	
	print session.retrlines('LIST')
	session.quit()
	


def usage():
	print "UploadFtp version 1.0 Created By PolymorphicCode 2014"
	print "./uploadFtp -file test.zip"
	print "./uploadFtp   ==> help"
	print "./uploadFtp --help ==> help"
	print "./uploadFtp --list ==> list all content of the parent directory"
	print "./uploadFtp --folder [exist folder name] --list  ==> list all content of folder"
	print "./uploadFtp --list --folder [exist foldername] ==> list all content of folder"
	print "./uploadFtp --file test.zip --folder [exist folder name]  ==> upload test.zip file into exist folder"
	print "./uploadFtp --file test.zip --newfolder [new folder name] ==> upload test.zip file into new created folder"



if __name__ == "__main__":
	
	  
	
	  if len(sys.argv) == 1:
	  	 usage()
	  	 exit(0)
	  
	  elif len(sys.argv) == 2: 
	  	 if  sys.argv[1] == '--help':
	  	 	usage()
	  	 	exit(0)
	  	 elif sys.argv[1] == '--list'	:
	  	 	getList(filedirectory = None)
	  	 	exit(0)
	  	 else :
	  	 	print "Not correct Usage: Please Type --help option"
	  	 	exit(0)
	  	 	
	  elif len(sys.argv) == 3 :
	  		if sys.argv[1] == '--help':
	  			usage()
	  	 		exit(0)
	  		elif sys.argv[1] == '--file':
	  			upload(sys.argv[2],None,0) # filedirectory is default zero this means current directory
	  			exit(0)
	  		else:
	  			print "Not correct Usage: Please Type --help option"
	  	 		exit(0)
	  elif len(sys.argv) == 4:
	  		if sys.argv[1] == '--folder' and sys.argv[3] == '--list' :# --folder  --list
	  			getList(sys.argv[2])
	  			exit(0)
	  		elif sys.argv[1] == '--list' and sys.argv[2] == '--folder' :
	  			getList(sys.argv[3])
	  			exit(0)

	  elif len(sys.argv) == 5:
	  		if sys.argv[1] == '--file' and sys.argv[3] == '--folder':
	  			upload(sys.argv[2],sys.argv[4],folderstate=1)
	  			exit(0)
	  		elif sys.argv[1] == '--file' and sys.argv[3] == '--newfolder':
	  			upload(sys.argv[2],sys.argv[4],folderstate =2)
	  			exit(0)
	  else:
	  	print "too many parameters not correct usage : --help option"
	  	exit(0)
	  	 	
