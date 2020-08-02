import logging
import smtplib
import time
from email.mime.text import MIMEText

def send_email(data):
    #设置服务器所需信息
    #163邮箱服务器地址
    mail_host = 'smtp.163.com'
    #163用户名
    mail_user = 'lixiupei1116@163.com'
    #密码(部分邮箱为授权码)
    mail_pass = 'DCJWIXOIIVFXCQDS'
    #邮件发送方邮箱地址
    sender = 'lixiupei1116@163.com'
    #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['lixiupei1116@163.com']

    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #设置email信息
    #邮件内容设置
    message_info = '已于'+timenow+'数据库更完成数据如下\n'+str(data)
    message = MIMEText(message_info,'plain','utf-8')
    #邮件主题
    message['Subject'] = '数据库更新'
    #发送方信息
    message['From'] = sender
    #接受方信息
    message['To'] = receivers[0]

    #登录并发送邮件
    try:
      smtpObj = smtplib.SMTP()
      #连接到服务器
      smtpObj.connect(mail_host,25)
      #登录到服务器
      smtpObj.login(mail_user,mail_pass)
      #发送
      smtpObj.sendmail(
           sender,receivers,message.as_string())
      #退出
      smtpObj.quit()
      logging.info("发送完成")
    except smtplib.SMTPException as e:
      logging.error('error',e) #打印错误