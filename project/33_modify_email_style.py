# smtplib
# email

import smtplib
from email.mime.text import MIMEText
from email.header import Header

try:
    # login account
    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_obj.starttls()  # 启动 TLS 加密
    smtp_obj.login('xueda3122356@gmail.com', 'jishtrpmnetbfhvl')


    # 邮件内容
    mail_text = '''
    <h1 style="color:blue">This is a email using html to display</h1>
    <p>This is the main body of the email</p>
    <p><a href = "http://www.baidu.com">This is a super link to baidu</a></p>
'''
    msg_body = MIMEText(mail_text, 'html')
    msg_body['From'] = Header('Test Department')
    msg_body['Subject'] = Header('Test Email')


    # 发送邮件
    smtp_obj.sendmail('xueda3122356@gmail.com', ['xueda3122356@hotmail.com'], msg_body.as_string())
    print("Email sent successfully!")

except smtplib.SMTPException as e:
    print(f"Error: {e}")

finally:
    smtp_obj.quit()
