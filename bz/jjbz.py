#!/bin/python3

import requests
#User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
if __name__ == "__main__":
    url = "https://bz.zzzmh.cn/#anime"
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'
    with open('a.html','w') as fp:
        fp.write(response.text)

