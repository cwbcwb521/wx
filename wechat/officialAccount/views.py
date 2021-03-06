from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import hashlib
from django.views.decorators.csrf import csrf_exempt

# logger
import logging

logger = logging.getLogger('django')

from officialAccount.receiveMessages import receive
from officialAccount.receiveMessages import autoReplayMessage
from officialAccount.basic import getAccessToken

# thread
import threading

@csrf_exempt
def handle(request):
    if request.method == "GET":
        # 接收微信服务器get请求发过来的参数(验证用)
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        logger.debug('wx connect check begin')
        logger.debug('signature: ' + signature)
        logger.debug('timestamp: ' + timestamp)
        logger.debug('nonce: ' + nonce)
        logger.debug('echostr: ' + echostr)

        # 服务器配置中的token
        token = 'wxtest'
        # 把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist]).encode("utf8")
        hashstr = hashlib.sha1(hashstr).hexdigest()
        logger.debug('hashstr: ' + hashstr)
        logger.debug('wx connect check ended')

        # start threading run accesstoken
        logger.debug('run accesstoken start')
        t = threading.Thread(target=getAccessToken.Basic.run, args=())
        t.start()
        logger.debug('run accesstoken end')

        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("fail")
    elif request.method == "POST":
        json_data = request.body
        logger.debug('post json data: ' + str(json_data))
        # xml convert to json data
        rec_msg = receive.parse_xml(json_data)
        if rec_msg is not None and rec_msg.MsgType == 'text':
            # get accessToken
            if rec_msg.Content.decode("utf8") == 'get accessToken':

                logger.debug('create menu success')
                return autoReplayMessage.replayTextMsg(rec_msg, '获取成功')
            logger.debug('receive text msg, start auto reply')
            # replay text
            return autoReplayMessage.replayTextMsg(rec_msg)
        else:
            # pic
            logger.debug('暂且不处理 ')
            return HttpResponse("success")
