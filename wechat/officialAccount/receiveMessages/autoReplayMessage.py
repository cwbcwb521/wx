from django.http import JsonResponse, HttpResponse
import requests

# logger
import logging

logger = logging.getLogger('django')

from officialAccount.receiveMessages import reply


def replayTextMsg(rec_msg, custom=None):
    if custom is None:
        content = autoReplay(rec_msg.Content)
    else:
        content = custom
    logger.debug('auto replay content: ' + content)
    if content is None:
        # no data
        logger.debug('content is None')
        return HttpResponse("success")
    to_user = rec_msg.FromUserName
    from_user = rec_msg.ToUserName
    reply_msg = reply.TextMsg(to_user, from_user, content)
    return HttpResponse(reply_msg.send())


# 自动回复
def autoReplay(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + msg.decode("utf8")
    req = requests.get(url)
    jsonData = req.json()
    jsonData['content'] = jsonData['content'].replace('菲菲', '小确丧')
    if jsonData['result'] == 0:
        logger.debug('get auto reply info')
        return jsonData['content']
    else:
        return None
