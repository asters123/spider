#!/bin/python3
import requests
import re
from lxml import etree
#User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
#url = https://fanyi.baidu.com/sug
#post
#query : k
#post(data是一个字典)
if __name__ == "__main__":
    url = "https://www.qidian.com/rank"
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }
###################################################
    LIST_PM = []
    NUM = 1
    NUM_ADDRESS = ''
    NUM_AUTHOR = ''
    NUM_TYPE = ''
    NUM_INFO = ''
####################################################
    response_qidian = requests.get(url=url,headers=headers).text
    re_qidian_num_name = '<a href="//book.qidian.com/info/.*?" target="_blank" data-eid="qd_C40" data-bid=".*?">.*?</a>'
    #书名
    NUM_NAME = re.findall(re_qidian_num_name,response_qidian,re.S)[0][100:-4]
    re_qidian_num_address = '<a href="//book.qidian.com/info/.*?" target="_blank" data-eid="qd_C40" data-bid="'
    #地址
    NUM_ADDRESS ="https:" +re.findall(re_qidian_num_address,response_qidian,re.S)[0][9:-46]
    NUM_ONE = requests.get(url=NUM_ADDRESS,headers=headers).text
    re_qidian_num_type = '<a href="//www.qidian.com/.*?" class="red" target="_blank" data-eid="qd_G10">.*?</a>'
    #类型
    NUM_TYPE = re.findall(re_qidian_num_type,NUM_ONE,re.S)[0][-6:-4]
    re_qidian_info = '<div class="book-intro">.*?</div>'
    NUM_INFO = re.findall(re_qidian_info,NUM_ONE,re.S)[0][114:-85].replace('<br>','\n')
    print(NUM_INFO)



    LIST_PM.append(NUM)
    LIST_PM.append(NUM_NAME)
    LIST_PM.append(NUM_ADDRESS)
    LIST_PM.append(NUM_TYPE)
    LIST_PM.append(NUM_INFO)

    print(LIST_PM)








    '''
        with open('qd.html','w') as fp:
            fp.write(response)
    '''
