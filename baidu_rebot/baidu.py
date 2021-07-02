#!/bin/python3

import requests
import execjs
import time
import random

#========================get_QR_code========================================
#目的:获得sign
#====execjs使用方法=====
#实例化一个node对象
node = execjs.get()
#js源文件编译
compile_get_gid = node.compile(open('./js/get_gid.js',encoding='utf-8').read())
#执行js
gid = compile_get_gid.eval('get_gid()')
print(gid)
#====execjs结束=====


tt = int(time.time()*1000)
print(tt)

callback = "tangram_guid_"+str(tt-random.randint(2000,7000))
print(callback)

_ = tt+random.randint(7,13)
print(_)
lp = "pc"
qrloginfrom = "pc"
apiver = "v3"
tpl = "netdisk"


    #
    ##lp:固定
    #lp: pc
    ##qrloginfrom固定
    #qrloginfrom: pc
    #gid: js生成(已解决)
    #callback: tangram_guid_1624150981823
    ##apiver固定
    #apiver: v3
    ##tt时间戳
    #tt: 1624150983553
    ##tpl固定
    #tpl: netdisk
    ##也是时间戳 比tt大
    #_: 1624150983561
    #
    #
    ##    lp: pc
    ##    qrloginfrom: pc
    ##    gid: EB93098-737C-4E4A-9953-86B54AAABF2A
    ##    callback: tangram_guid_1624152442228
    ##    apiver: v3
    ##    tt: 1624152447275
    ##    tpl: netdisk
    ##    _: 1624152447286
    #
    #
    #
    #
    #BAIDUID=""
    #HOSUPPORT=""
    #HOSUPPORT_BFESS=""
    #pplogid=""
    #pplogid_BFESS=""
    #
    #get_qr_code_cookie = "BAIDUID="+BAIDUID+"; HOSUPPORT="+HOSUPPORT+"; HOSUPPORT_BFESS="+HOSUPPORT_BFESS+"; pplogid="+pplogid+"; pplogid_BFESS="+pplogid_BFESS
    #print(get_qr_code_cookie)
    #
    #
    ##========================QR_code========================================
    #sign = ""
    #qr_code_url = "https://passport.baidu.com/v2/api/qrcode?sign="+sign+"&lp=pc&qrloginfrom=pc"
    #print("=============================================================================")
    #print(qr_code_url)
    #print("=============================================================================")
    #
    #
    #
    #
    ##Cookie
    #qr_code_cookie = "BAIDUID="+BAIDUID+"; HOSUPPORT="+HOSUPPORT+"; HOSUPPORT_BFESS="+HOSUPPORT_BFESS+"; pplogid="+pplogid+"; pplogid_BFESS="+pplogid_BFESS
    #print("qr_code的cookie是====="+qr_code_cookie)
    #
