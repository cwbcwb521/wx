# -*- coding: utf-8 -*-
# filename: menu.py
import urllib.request
from officialAccount.basic import getAccessToken
from django.http import JsonResponse, HttpResponse
import hashlib
from django.views.decorators.csrf import csrf_exempt

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# logger
import logging
logger = logging.getLogger('django')


class Menu(object):
    def __init__(self):
        pass

    def create(self, postData, accessToken):
        logger.debug('create menu')
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, str):
            postData = postData.encode('utf-8')
        urlResp = urllib.request.urlopen(url=postUrl, data=postData)
        logger.debug(urlResp.read())

    def query(self, accessToken):
        logger.debug('query menu')
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url=postUrl)
        logger.debug(urlResp.read())

    def delete(self, accessToken):
        logger.debug('delete menu')
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url=postUrl)
        logger.debug(urlResp.read())

    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        logger.debug('get current self menu info')
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url=postUrl)
        logger.debug(urlResp.read())


@csrf_exempt
def createmenu(request):
    logger.debug('start menu option')
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "type": "click",
                "name": "开发指引",
                "key":  "mpGuide"
            },
            {
                "name": "公众平台",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "更新公告",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "接口权限说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "返回码说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
                    }
                ]
            },
            {
                "type": "media_id",
                "name": "旅行",
                "media_id": "z2zOokJvlzCXXNhSjF46gdx6rSghwX2xOD5GUV9nbX4"
            }
          ]
    }
    """

    logger.debug('get access token')
    accessToken = getAccessToken.Basic().get_access_token()
    #myMenu.delete(accessToken)

    logger.debug('start create menu')
    myMenu.create(postJson, accessToken)

    return HttpResponse("success")