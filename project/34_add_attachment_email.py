# smtplib
# email

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

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


    # 添加附件
    file = MIMEApplication(open('./generate_data/21_word2pdf.pdf', 'rb').read())
    file.add_header('Content-Disposition', 'attachment', filename='wp.pdf')

    # 封装邮件主体
    multi_part = MIMEMultipart()
    multi_part.attach(msg_body)
    multi_part['From'] = Header('Test Department')
    multi_part['Subject'] = Header('Test Email with attachment')

    # 封装附件
    multi_part.attach(file)

    # 发送邮件
    smtp_obj.sendmail('xueda3122356@gmail.com', ['xueda3122356@hotmail.com'], multi_part.as_string())
    print("Email sent successfully!")

except smtplib.SMTPException as e:
    print(f"Error: {e}")

finally:
    smtp_obj.quit()