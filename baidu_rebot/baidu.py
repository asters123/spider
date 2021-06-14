#!/bin/python3
from os import write
from baidu_config import *
import requests
import re




cookie = 'BDUSS='+BDUSS+'; STOKEN='+STOKEN

headers = {

    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
#    'Cookie':cookie,
    'Cookie':cookie,
    'Host':'pan.baidu.com',
    'Pragma':'no-cache',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
        }

url = 'https://pan.baidu.com/api/list'



res = requests.get(url=url,headers=headers)
res.encoding = 'utf-8'

re_file_name = '"server_filename":".*?","'
file_name_all = re.findall(re_file_name,res.text,re.S)
i = 0
for a in file_name_all:
    file_name = file_name_all[i][19:-3]
    i = i+1
    print((file_name))
