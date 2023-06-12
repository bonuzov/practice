import subprocess
import smtplib


def CheckFile():
    file = open('old_ip.txt', 'r')
    if ip != file.read():
        file.close()
        open('old_ip.txt', 'w').close()
        file = open('old_ip.txt', 'w')
        file.write(ip)
        file.close()
        return True
    return False


def SendMail():
    content = ip
    connection = smtplib.SMTP_SSL('smtp.server', 465)
    connection.login('login, 'password')
    connection.sendmail('sender email', 'recipient email', content)
    connection.quit()


def GetIp():
    open('new_ip.txt', 'w').close()
    subprocess.call('getip.bat')


GetIp()
ip = open('new_ip.txt', 'r').read()

if CheckFile() == True:
    SendMail()