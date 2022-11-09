import poplib
from email.parser import Parser

email = '2537239220@qq.com'
password = 'tbwzcfttpltudjge'
pop3_server = 'pop.qq.com'

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

# 身份认证:
server.user(email)
server.pass_(password)

print('邮件数量: %s. 占用空间: %s' % server.stat())
resp, mails, octets = server.list()
print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)

server.quit()