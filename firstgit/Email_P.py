import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email import encoders

host=input("SMTP Server : ")
port=input("SMTP Port : ")
sender=input("Sender Mail : ")
recipient=input("recipient Mail : ")
r_path=input("Real path Plz : ")

def search(dirname):
    filenames = os.listdir(dirname)
    i=1
    for filename in filenames:
        ifile = os.path.join(dirname, filename)
        #host='10.10.20.116' #external
        #port='25' #smtp port
        #htmlfile='c:\mail.html' # 메일 내용 파일
        #ifile='c:/ConsoleApplication2.exe' #파일 첨부

        #sender='hunho88@external.co.kr' #sender email address
        #recipient='administrator@januber.co.kr' #recipient email address

        msg=MIMEMultipart('alternative')
        msg['Subject']='Sample '+str(i)
        msg['From']=sender
        msg['To']=recipient

        # Create MIMEHtml
        #htmlF=open(htmlfile,'rb')
        #htmlPart=MIMEText(htmlF.read(),'html',_charset='utf-8')
        #htmlF.close()

        # 파일 첨부 인코딩
        part=MIMEBase('application','octet-stream')
        part.set_payload(open(ifile,'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=%s'%os.path.basename(ifile))

        # 파일 첨부
        #msg.attach(htmlPart)
        msg.attach(part)

        # 메일 전송
        s=smtplib.SMTP(host,port)
        #s.set_debuglevel(1) #debuging
        s.ehlo()
        s.ehlo()
        s.sendmail(sender,[recipient],msg.as_string())
        s.close()
        print("Transfer Complete")
        i=i+1

search(r_path)
