from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import hashlib
from django.views.decorators.csrf import csrf_exempt

# logger
import logging
logger = logging.getLogger('django')

from officialAccount.receiveMessages import receive
from officialAccount.receiveMessages import reply



@csrf_exempt
def handle(request):
    if request.method == "GET":
        # 接收微信服务器get请求发过来的参数(验证用)
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        logger.debug('wx connect check begin')
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
        logger.debug('wx connect check ended')

        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("fail")
    elif request.method == "POST":
        json_data = request.body
        logger.debug('post json data: '+json_data)
        # xml convert to json data
        rec_msg = receive.parse_xml(json_data)
        if rec_msg is not None and rec_msg.MsgType == 'text':
            logger.debug('receive text msg')
            # replay text
            content = reply.autoReplay(rec_msg.Content)
            logger.debug('auto replay content: '+content)
            if content is None:
                # no data
                return "success"
            to_user = rec_msg.FromUserName
            from_user = rec_msg.ToUserName
            reply_msg = reply.TextMsg(to_user, from_user, content)
            return reply_msg.send()
        else:
            # pic
            logger.debug('暂且不处理 ')
            return "success"

