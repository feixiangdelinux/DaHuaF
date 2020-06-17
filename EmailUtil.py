import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_msg(to_addr, title, content):
    from_addr = '957493412@qq.com'
    password = 'pdtsanllybzwbdgg'
    smtp_server = 'smtp.qq.com'
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr('957493412@qq.com')
    msg['Subject'] = Header(title, 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


send_msg('1421760774@qq.com', '大话西游', '200环完成')
