from ftplib import FTP

ftp=FTP('speedtest.tele2.net')
ftp.login()
ftp.retrlines('LIST')
filename='1MB.zip'
files=open("ftp_file.txt","wb")
ftp.retrbinary('RETR {}'.format(filename),files.write)
files.close()
