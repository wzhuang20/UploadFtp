UploadFtp
=========

UploadFtp upload file to ftp server 
  Usage:
./uploadFtp -file test.zip
./uploadFtp   ==> help
./uploadFtp --help ==> help
./uploadFtp --list ==> list all content of the parent directory
./uploadFtp --folder [exist folder name] --list  ==> list all content of folder
./uploadFtp --list --folder [exist foldername] ==> list all content of folder
./uploadFtp --file test.zip --folder [exist folder name]  ==> upload test.zip file into exist folder
./uploadFtp --file test.zip --newfolder [new folder name] ==> upload test.zip file into new created folder

Config.ini dosyası icerisinde ayarlar su anlık yapılmıs fakat eger siz baska bır ftp serveri uzerinde upload etmek isterseniz bu dosya uzerindeki ilgili yerleri ayarlamaniz gerekecektir.

Config.ini :

[FTP Server]
host=ftp.****.com
user=*****
pass=*****



  Created  by PolymorphicCode

 


