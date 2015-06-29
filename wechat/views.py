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
import logging

def loglist(filename):
    log = logging.getLogger()
    handler = logging.handlers.TimedRotatingFileHandler('templates/logs/' + '/' + filename + '.log',
                                                        when="d",
                                                        interval=1,
                                                        backupCount=5)
    format = "%(asctime)s - %(levelname)s: %(message)s"
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
    handler.suffix = "_%Y%m%d"
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    return log


log = loglist('WeChat')
@csrf_exempt
def Index(request):
    a = request.POST
    print "============="
    log.warning("index")
    log.info(a)
    try:
        tousername = a["AddMsgList[0][ToUserName]"]
        print "ToUserName:", a["AddMsgList[0][ToUserName]"]
        print "FromUserName:", a["AddMsgList[0][FromUserName]"]
        print "MsgId:", a["AddMsgList[0][MsgId]"]
        print "Content:", a["AddMsgList[0][Content]"]

    except:
        pass
    # because someone send link with msg
    try:
        tousername = a["AddMsgList[1][ToUserName]"]
        print "ToUserName:", a["AddMsgList[1][ToUserName]"]
        print "FromUserName:", a["AddMsgList[1][FromUserName]"]
        print "MsgId:", a["AddMsgList[1][MsgId]"]
        print "Content:", a["AddMsgList[1][Content]"]
    except:
        pass
    # print "SKey:", a["SKey"]
    # print "imgURL: https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetmsgimg?&MsgID="+a["AddMsgList[0][MsgId]"]
    print "================"
    # https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetmsgimg?&MsgID=7822432876888295620&skey=%40crypt_f317f0c4_0309c0c4d1d4e07715974601d7611ee5
    return HttpResponse('ok')


@csrf_exempt
def QR(request):
    a = request.POST
    log.warning("QR")
    log.info(a)
    print "Login image:", a
    return HttpResponse(a)


@csrf_exempt
def userAvatar(request):
    a = request.POST
    log.warning("userAvatar")
    log.info(a)
    print "userAvatar:", a['userAvatar']
    return HttpResponse(a)


@csrf_exempt
def userinfo(request):
    a = request.POST
    log.warning("MyInfo")
    log.info(a)
    print "UserName:", a['UserName']
    print "img:", a['img']

    return HttpResponse(a)

@csrf_exempt
def userDetail(request):
    a = request.POST
    log.warning("userinfo")
    log.info(a)
    print "UserName:", a
    # print "img:", a['img']

    return HttpResponse(a)


