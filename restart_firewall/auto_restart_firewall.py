#!/bin/python3

import re
import requests
#User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
if __name__ == "__main__":
    url = "http://10.0.0.1"
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }
    data_login = {
        'luci_username':'root',
        'luci_password':'000000'
            }
    session = requests.Session()
    session.post(url=url,headers=headers,data=data_login)
    url_restart_firewall = 'http://10.0.0.1/cgi-bin/luci/admin/network/firewall/custom'
    token_text = session.get(url=url_restart_firewall,headers=headers).text
    re_token = 'name="token" value=".*?" />'
    token = re.findall(re_token,token_text,re.S)[0][20:-4]
    print(token)
#token: 661abd68fd77afc1fc3c18b1d45ee552
#cbi.submit: 1
#cbid.firewall.1._custom: # This file is interpreted as shell script.
#
## Put your custom iptables rules here, they will
#
## be executed with each firewall (re-)start.
#
#
#
## Internal uci firewall chains are flushed and recreated on reload, so
#
## put custom rules into the root chains e.g. INPUT or FORWARD or into the
#
## special user chains, e.g. input_wan_rule or postrouting_lan_rule.
#
#iptables -t nat -A PREROUTING -p udp --dport 53 -j REDIRECT --to-ports 53
#
#iptables -t nat -A PREROUTING -p tcp --dport 53 -j REDIRECT --to-ports 53
