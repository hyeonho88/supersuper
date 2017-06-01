#-*-coding:utf-8-*-
import smtplib
import mimetypes

from email.mime.text import MIMEText
from email import utils
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

textfile = "shorttext.txt"
textfile = u"안녕하세요.txt"
smtp_server ='10.10.20.116'
smtp_port=25
testfile = open(textfile,'w')
testfile.write('파이썬이다.')
testfile.close()
imagefile='c:\score1.jpg'
fp=open(textfile,'rb')

imageF=open(imagefile,'rb')
imagePart=MIMEImage(imageF.read())
imageF.close()
msg=MIMEImage(fp.read(),"html",_charset="utf-8")
msg2=MIMEBase('multipart','mixed')

fp.close()

me= 'hunho88@external.co.kr'
you='administrator@januber.co.kr'

#MIME base

msg['Subject']="이건 파이썬으로 보내는 이메일"
msg['From']=me
msg['To']=you
msg['Date']=utils.formatdate(localtime=1)
msg2.attach(imagePart)
s=smtplib.SMTP(smtp_server,smtp_port)
s.ehlo()
s.ehlo()

#s.login("hunho88@external.co.kr","dpffl88!")
s.sendmail(me,you,msg.as_string())
s.quit()
