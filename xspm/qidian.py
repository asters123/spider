#!/bin/python3
import requests
import re
import os
#User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
#url = https://fanyi.baidu.com/sug
#post
#query : k
#post(data是一个字典)
if __name__ == "__main__":
    path = './起点排行.txt'
    if os.path.exists(path):
        os.remove(path)
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
    #书名
    re_qidian_num_address = '<a href="//book.qidian.com/info/.*?" target="_blank" data-eid="qd_C40" data-bid="'
    #地址
    NUM_ADDRESS ='<a class="name" href="' +re.findall(re_qidian_num_address,response_qidian,re.S)[0][9:-1] +'"'
#    print(NUM_INFO)

    re_qidian_1_10 = '<a class="name" href="//book.qidian.com/info/.*?" target="_blank" data-eid="qd_C40" data-bid="'
    NUM_1_10_list = re.findall(re_qidian_1_10,response_qidian,re.S)
    NUM_1_10_list.insert(0,NUM_ADDRESS)
#print(NUM_2_9_list[0:9])
    #print(NUM_1_10_list[1])
    i = 0
    while i<10 :
        LIST_PM_NUM = []
        num_name_url = 'https:'+NUM_1_10_list[i][22:-46]
        print(i+1, num_name_url)
        i = i+1
        #地址
        num_name_url_response = requests.get(url=num_name_url,headers=headers).text
        re_num_name = '<h1>.*?</em>'
        #名字
        num_name = re.findall(re_num_name,num_name_url_response,re.S)[0][34:-5]
        re_num_name_type = '<a href="//www.qidian.com/.*?" class="red" target="_blank" data-eid="qd_G10">.*?</a>'
        #类型
        num_name_type = re.findall(re_num_name_type,num_name_url_response,re.S)[0][-6:-4]
        re_num_name_info = '<div class="book-intro">.*?</div>'
        num_name_info = re.findall(re_num_name_info,num_name_url_response,re.S)[0][114:-85].replace('<br>','\n')
        re_num_name_month_num = '<p class="num"><i id="monthCount">.*?</i></p>'
        num_name_month_num = re.findall(re_num_name_month_num,num_name_url_response,re.S)[0][34:-8]

        LIST_PM_NUM.append(i+1)
        LIST_PM_NUM.append(num_name)
        LIST_PM_NUM.append(num_name_type)
        LIST_PM_NUM.append(num_name_info)
        LIST_PM_NUM.append(num_name_month_num)
        LIST_PM.append(LIST_PM_NUM)
    #print(LIST_PM)
    i = 0
    while i<10 :
        print('第{0}名'.format(i+1))
        print('名字：' +LIST_PM[i][1])
        print('类型：' +LIST_PM[i][2])
        print('简介：\n' +LIST_PM[i][3])
        print('月票：' +LIST_PM[i][4])
        print('=====================================')
        with open('起点排行.txt','a',encoding='utf-8') as fp:
            fp.write('第{0}名\n'.format(i+1))
            fp.write('名字：' +LIST_PM[i][1] +'\n')
            fp.write('类型：' +LIST_PM[i][2] +'\n')
            fp.write('简介：\n' +LIST_PM[i][3] +'\n')
            fp.write('月票：' +LIST_PM[i][4] +'\n')
            fp.write('=====================================\n')
        i = i+1

