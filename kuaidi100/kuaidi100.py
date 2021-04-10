#!/bin/python3
import random
import requests
import json
#User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
if __name__ == "__main__":
    value1 = str(random.random())
    url = "https://www.kuaidi100.com/query?type=yunda&postid=4313515008449&temp=" +value1 +"&phone="
    headers = {
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Referer":"https://www.kuaidi100.com/?from=openv",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    }
    response = requests.get(url=url,headers=headers).text
    json_response = json.loads(response)
    for num in json_response["data"]:
        print(num["time"] +"," +num["ftime"] +"," +num["context"] +"," +num["location"])
