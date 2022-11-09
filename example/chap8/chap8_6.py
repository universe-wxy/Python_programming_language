from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

def send_mail(sender_qq='',pwd='',receiver='',mail_title='',mail_content=''):
    host_server = 'smtp.qq.com'
    sender_qq_mail = sender_qq+'@qq.com'

    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    sender_qq = '3458466534'
    pwd = 'crfqrlhijeqrchfh'
    receiver='2537239220@qq.com'
    mail_content = 'Hello world'
    mail_title = 'a tester that you know'
    for i in range(2):
         send_mail(sender_qq=sender_qq,pwd=pwd,receiver=receiver,mail_title=mail_title,mail_content=mail_content)