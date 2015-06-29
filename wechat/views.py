__author__ = 'liuzheng'
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import os
import sys
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def Index(request):
    a = request.POST
    print "ToUserName:", a["AddMsgList[0][ToUserName]"]
    print "FromUserName:", a["AddMsgList[0][FromUserName]"]
    print "MsgId:", a["AddMsgList[0][MsgId]"]
    print "Content:", a["AddMsgList[0][Content]"]
    # print "SKey:", a["SKey"]
    # print "imgURL: https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetmsgimg?&MsgID="+a["AddMsgList[0][MsgId]"]
    print "================"
    # https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetmsgimg?&MsgID=7822432876888295620&skey=%40crypt_f317f0c4_0309c0c4d1d4e07715974601d7611ee5
    return HttpResponse(json.dumps(a))


@csrf_exempt
def QR(request):
    a = request.POST
    print "Login image:", a
    return HttpResponse(a)


@csrf_exempt
def userinfo(request):
    a = request.POST
    print "UserName:", a['UserName']
    print "img:", a['img']

    return HttpResponse(a)