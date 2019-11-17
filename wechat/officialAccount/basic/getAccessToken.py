# -*- coding: utf-8 -*-
# filename: basic.py
import urllib.request
import time
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# logger
import logging
logger = logging.getLogger('django')


class Basic:
    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0

    def __real_get_access_token(self):
        logger.debug('[method]start get access token')
        appId = "wxd94535e4e58ee0ab"
        appSecret = "931a91942a36bf9fd6887476d2fbd6c3"
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
                   "client_credential&appid=%s&secret=%s" % (appId, appSecret))
        urlResp = urllib.request.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']
        logger.debug('[method] get access token over')
        logger.debug('[method] __accessToken : ' + str(self.__accessToken))
        logger.debug('[method] __leftTime : ' + str(self.__leftTime))

    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
            return self.__accessToken
        else:
            return self.__accessToken

    def run(self):
        while (True):
            if self.__leftTime > 10:
                time.sleep(5)
                self.__leftTime -= 5
            else:
                self.__real_get_access_token()
