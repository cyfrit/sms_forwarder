from urllib3 import PoolManager
import config
import logging
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

def forward_to_email(number,content,timestamp):
    if config.email_enable:
        # 构造邮件内容
        subject = 'SMS Forwarder: New message from {}'.format(number)
        message_body = 'Number: {}\nContent: {}\nTimestamp: {}'.format(number, content, timestamp)
        message = MIMEText(message_body, 'plain', 'utf-8')
        message['From'] = formataddr((str(Header(config.email_from, 'utf-8')), config.email_user))
        message['To'] = Header(config.email_to, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')

        # 连接 SMTP 服务器并发送邮件
        try:
            if config.email_ssl:
                server = smtplib.SMTP_SSL(config.email_host, config.email_port)
            else:
                server = smtplib.SMTP(config.email_host, config.email_port)
            server.login(config.email_user, config.email_password)
            server.sendmail(config.email_from, [config.email_to], message.as_string())
            logging.info('Forwarded to email')
        except Exception as e:
            logging.error('Failed to forward to email: {}'.format(e))
        finally:
            server.quit()
        

def forward_to_telegram(number,content,timestamp):
    if(config.tg_enable):
        url = "https://{}/bot{}/sendMessage".format(config.tg_api_host, config.tg_bot_token)
        message = 'Number:{}\nContent: {}\nTimestamp: {}'.format(number, content, timestamp)
        data = {'chat_id': config.tg_user_id, 'text': message}
        http = PoolManager()
        response = http.request('POST', url, fields=data)
        if response.status == 200:
            logging.info('Forwarded to telegram')
        else:
            logging.error('Failed to forward to telegram: {}'.format(response.data))