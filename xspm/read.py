import requests
#User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
#post(data是一个字典)
if __name__ == "__main__":
    url = "https://read.qidian.com/chapter/jeeUVdmTKNzv7_WH3wfEdQ2/eSlFKP1Chzg1"
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }
    response = requests.get(url=url,headers=headers).text
    with open('c.html','w') as fp:
        fp.write(response)
