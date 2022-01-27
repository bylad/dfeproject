from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import socket
import requests


HTTP_LINK = 'http://127.0.0.1:8000'


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address


def check_link(ip):
    http_address = f'http://{ip}:8000'
    try:
        requests.head(http_address)
        return http_address
    except requests.ConnectionError:
        return http_address[:-5]  # http without port num


def sending(app, news_id, title):
    msg = MIMEMultipart()
    # recipients = ['nhaymina@adm-nao.ru', 'btcyrenzhapov@adm-nao.ru']
    recipients = ['btcyrenzhapov@adm-nao.ru']
    msg['To'] = ', '.join(recipients)
    msg['From'] = 'dfei@adm-nao.ru'
    msg['Subject'] = 'Новые стат.данные'

    ip_addr = get_ip()
    http_link = check_link(ip_addr)
    body_text = f'Добавлена новость<br><a href="{HTTP_LINK}/{app}/{news_id}/">{title}</a>'

    body = MIMEText(body_text, 'html', 'utf-8')
    msg.attach(body)  # add message body (text or html)

    s = smtplib.SMTP('mail.adm-nao.ru')
    s.sendmail(msg['From'], recipients, msg.as_string())
    s.close()
