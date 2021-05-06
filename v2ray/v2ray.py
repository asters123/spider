#!/bin/python3
import requests
import re
from time import sleep
#User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
#url = https://fanyi.baidu.com/sug
#post
#query : k
#post(data是一个字典)
if __name__ == "__main__":
#=====================================获取邮箱部分=========================================================
    session_linshi_mail = requests.Session()
    session_linshi_mail.get("https://www.linshiyouxiang.net")
    url_query_mail = "https://www.linshiyouxiang.net/api/v1/mailbox/keepalive"
    headers = {
        'referer':'https://linshiyouxiang.net/',
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
            }
    url_query_mail_text = session_linshi_mail.get(url=url_query_mail,headers=headers).text
    re_mail = 'mailbox":".*?","'
    mail_qianzhui = re.findall(re_mail,url_query_mail_text,re.S)[0][10:-3]
    print('前缀为：'+mail_qianzhui)
    mail_linshi = mail_qianzhui+'@powerencry.com'
    print('邮箱为：'+mail_linshi)
#====================================邮箱部分结束========================================================

#====================================发送验证码======================================================
    url_send_code= "https://www.franxx.cloud/auth/send"
    email_date = {
        'email':mail_linshi
            }
    requests.post(url=url_send_code,data=email_date,headers=headers)

#=====================================接收验证码========================================================

    url_mail_linshi_code = 'https://www.linshiyouxiang.net/api/v1/mailbox/'+ mail_qianzhui
    print("接受邮件地址为："+ url_mail_linshi_code)
    while True:
        mail_linshi_code = requests.get(url=url_mail_linshi_code,headers=headers).text
        print(mail_linshi_code)
        sleep(2)
        if mail_linshi_code[1] == '{' :
            print("接收到验证码邮件")
            break
#    print(mail_linshi_code)
    re_sid = 'id":".*?","from"'
    mail_code_bianma = re.findall(re_sid,mail_linshi_code,re.S)[0][5:-8]
    print("验证码邮件地址编码："+ mail_code_bianma)
    url_mail_code = 'https://www.linshiyouxiang.net/mailbox/'+ mail_qianzhui+'/'+ mail_code_bianma
    print("验证码邮件地址为："+ url_mail_code)
    code_response = requests.get(url=url_mail_code,headers=headers).text
    #print(code_response)
    re_code = '<span style="font-family: &#39;Nunito&#39;, Arial, Verdana, Tahoma, Geneva, sans-serif;color: #ffffff;font-size: 20px;line-height: 30px;text-decoration: none;font-weight: 600;">.*?</span>'
    code = re.findall(re_code,code_response,re.S)[0][-13:-7]
    print("验证码为："+ code)

#=====================================注册========================================================

    url_register = 'https://www.franxx.cloud/auth/register'
    date_register = {
        'email':mail_linshi,
        'name':'asters',
        'passwd':'11111111',
        'repasswd':'11111111',
        'code':'',
        'emailcode':code
    }
    requests.post(url=url_register,headers=headers,data=date_register)


#=====================================登录========================================================
    url_login = "https://www.franxx.cloud/auth/login"
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }
    data_login = {
        'email':mail_linshi,
        'passwd':'11111111'
            }
    session = requests.Session()
    response = session.post(url=url_login,headers=headers,data=data_login)
    #print(response.status_code)

    url_user = 'https://www.franxx.cloud/user'
    user = session.get(url=url_user,headers=headers).text
    re_v2ray = '<button type="button" class="btn btn-v2ray round waves-effect waves-light copy-text" data-clipboard-text=".*?">'
    v2ray = re.findall(re_v2ray,user,re.S)[0][106:-2]
    print("v2ray订阅地址为："+ v2ray)












