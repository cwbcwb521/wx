from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import hashlib

import logging
logger = logging.getLogger('django')

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def handle(request):
    if request.method == "GET":
        # 接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        logger.debug('check begin')
        logger.debug('signature: ' +signature)
        logger.debug('timestamp: '+timestamp)
        logger.debug('nonce: '+nonce)
        logger.debug('echostr: '+echostr)

        # 服务器配置中的token
        token = 'wxtest'
        # 把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist]).encode("utf8")
        hashstr = hashlib.sha1(hashstr).hexdigest()
        logger.debug('hashstr: '+hashstr)
        logger.debug('check ended')

        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("fail")
    else:
        return HttpResponse("not get")
