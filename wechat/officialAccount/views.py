from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import hashlib

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def handle(request):
    if request.method == "GET":
        signature = request.GET.get("signature")
        timestamp = request.GET.get("timestamp")
        nonce = request.GET.get("nonce")
        echostr = request.GET.get("echostr")

        token = "wxtest"
        if signature is None:
            return HttpResponse("no info")
        create_list = [token, timestamp, nonce]
        create_list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, create_list)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)

        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("field")
    else:
        return HttpResponse("not get")
