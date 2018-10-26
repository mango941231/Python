import psutil
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
gpus = int(sys.argv[1])

def sendemail():
    sender = 'he1119197389@163.com'
    password = 'he941231'  #密码是邮箱界面‘设置’里的客户端授权密码
    host = 'smtp.163.com'
    receivers = ['15634218103@163.com']
    message = MIMEText('爬虫挂掉~', 'plain', 'utf-8')
    message['From'] = 'he1119197389@163.com'
    message['To'] = '15634218103@163.com'        #From、TO必须和前面的sender、receivers保持一致
    message['Subject'] = Header('我是标题~', 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(host, 465)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("发送邮件成功")
    except smtplib.SMTPException as e:
        print("发送邮件产生错误")
        print(e)
        smtpObj.close()


def abnor(g):
    while 1:
        pids = psutil.pids()
        if g not in pids:
            break
    sendemail()



if __name__ == '__main__':
    abnor(gpus)


