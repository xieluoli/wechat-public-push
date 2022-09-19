import json
from turtle import pos
import requests

data = {
    # 用户openid（todo）
    "touser": "xxx",
    # 模版id (todo)
    "template_id": "xxx",
    "url": "",
    # 小程序跳转页（todo）
    # "miniprogram": {
    #      "appid": "wx4515b3f722b53d87",
    #      "pagepath": "index?foo=bar"
    #  },       
    # "data": {
    #     "approval_id":{
    #         "value":"120220915100000",
    #         "color": "#173177"
    #     },
    #     "approval_type": {
    #         "value": "请假申请",
    #         "color": "#173177"
    #     },
    #     "applicant":{
    #         "value": "张三",
    #     },
    #     "reason":{
    #         "value":"家里有事",
    #     },
    #     "approver":{
    #         "value":"王总;李总",
    #     },
    #     "approval_opinion":{
    #         "value":"无"
    #     }
    # }
    "data": {
        "username":{
            "value":"张三",
            "color": "#173177"
        },
    		"company":{
            "value":"xxx公司"
        },
    		"department":{
            "value":"财务部"
        }
    }
}
data2 = json.dumps(data)

# 获取access_token
# todo
appid = 'xxx'
# todo
appsec = 'xxx'
get_access_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={appsecret}'
get_access_url = get_access_url.format(appid = appid, appsecret = appsec)
res = requests.get(get_access_url)

# 推送公众号消息
access = json.loads(res.text)
token = access['access_token']
post_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_data}'
post_url = post_url.format(access_data = token)
res = requests.post(url=post_url, data = data2)
