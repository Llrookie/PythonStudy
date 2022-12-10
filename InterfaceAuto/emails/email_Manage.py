import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class emailMange:
    def email_send(self,filename):
        # 定义SMTP服务器
        smtpserver = 'smtp.qq.com'
        # 发送邮件的用户以及授权码
        username = '******@qq.com'
        password = 'cngf******zbdhj'
        # 接受邮件的用户名,有多个以,分割，如receiver='ddd,fff,fds'
        receiver = '******@qq.com'
        # 创建邮件对象
        message = MIMEMultipart('related')
        subject = 'Python邮件发送学习日志'  # 邮件主题
        fujian = MIMEText(open(filename, 'rb').read(), 'html', 'utf-8')
        # 把邮件信息组装起来
        message['from'] = username
        message['to'] = receiver
        message['subject'] = subject
        message.attach(fujian)
        # 登录smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连接服务器
        smtp.login(username, password)  # 登录
        smtp.sendmail(username, receiver, message.as_string())  # 发送，发送方，接收方，发送内容
        smtp.quit()  # 关闭


if __name__ == '__main__':
    emailMange().email_send()
