from django.db import models
from django.contrib import admin

# Create your models here.
class QRcode(models.Model):
    url = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    cstrf = models.TextField(null=True)
    # need more info


class LoginUserInfo(models.Model):
    UserID = models.TextField()
    UserName = models.TextField()
    UserAvatar = models.TextField()
    UserStatus = models.BooleanField(default=0)


class ContactList(models.Model):
    # ID = models.CharField(max_length=40)
    # MyFriend = models.CharField(max_length=40)
    # UserName = models.CharField(max_length=70)
    # NickName = models.CharField(max_length=40)
    # RemarkName = models.CharField(max_length=40)
    # Alias = models.CharField(max_length=40)
    # Sex = models.CharField(max_length=4)
    # StarFriend = models.CharField(max_length=4)
    # PYQuanPin = models.CharField(max_length=40)
    # Province = models.CharField(max_length=40)
    # City = models.CharField(max_length=40)
    # Statues = models.CharField(max_length=40)
    # HideInputBarFlag = models.CharField(max_length=40)
    # OwnerUin = models.CharField(max_length=40)
    # HeadImgUrl = models.CharField(max_length=40)
    # tags = models.TextField()
    WhoseFriend = models.TextField()
    Alias = models.TextField()
    AppAccountFlag = models.TextField()
    AttrStatus = models.TextField()
    ChatRoomId = models.TextField()
    City = models.TextField()
    ContactFlag = models.TextField()
    DisplayName = models.TextField()
    HeadImgUrl = models.TextField()
    HideInputBarFlag = models.TextField()
    KeyWord = models.TextField()
    MemberCount = models.TextField()
    NickName = models.TextField()
    OwnerUin = models.TextField()
    Province = models.TextField()
    PYInitial = models.TextField()
    PYQuanPin = models.TextField()
    RemarkName = models.TextField()
    RemarkPYInitial = models.TextField()
    RemarkPYQuanPin = models.TextField()
    Sex = models.TextField()
    Signature = models.TextField()
    SnsFlag = models.TextField()
    StarFriend = models.TextField()
    Statues = models.TextField()
    Uin = models.TextField()
    UniFriend = models.TextField()
    UserName = models.TextField()
    VerifyFlag = models.TextField()


# u'ContactList[34][Alias]': [u'Sissi-e'],
# u'ContactList[34][HideInputBarFlag]': [u'0'],
# u'ContactList[34][OwnerUin]': [u'0'],
# u'ContactList[34][RemarkPYInitial]': [u'LD'],
# u'ContactList[34][ContactFlag]': [u'8195'],
# u'ContactList[34][PYQuanPin]': [u'xiaolanmao'],
# u'ContactList[34][UserName]': [u'@af763385bb3bde9c3287b28b80d337b3d9bb8c18296b033f11fce9eef17fb1fd'],
# u'ContactList[34][Province]': [u''],
# u'ContactList[34][ChatRoomId]': [u'0'],
# u'ContactList[34][UniFriend]': [u'0'],
# u'ContactList[34][City]': [u''],
# u'ContactList[34][NickName]': [u'\u5c0f\u61d2\u732b'],
# u'ContactList[34][Statues]': [u'0'],
# u'ContactList[34][VerifyFlag]': [u'0'],
# u'ContactList[34][SnsFlag]': [u'49'],
# u'ContactList[34][Signature]': [u''],
# u'ContactList[34][Uin]': [u'2538016042'],
# u'ContactList[34][HeadImgUrl]': [u'/cgi-bin/mmwebwx-bin/webwxgeticon?seq=628511340&username=@af763385bb3bde9c3287b28b80d337b3d9bb8c18296b033f11fce9eef17fb1fd&skey='],
# u'ContactList[34][DisplayName]': [u''],
# u'ContactList[34][RemarkName]': [u'\u9886\u5bfc\uff01'],
# u'ContactList[34][AttrStatus]': [u'71401573'],
# u'ContactList[34][AppAccountFlag]': [u'0'],
# u'ContactList[34][RemarkPYQuanPin]': [u'lingdao'],
# u'ContactList[34][KeyWord]': [u''],
# u'ContactList[34][PYInitial]': [u'XLM'],
# u'ContactList[34][MemberCount]': [u'0'],
# u'ContactList[34][Sex]': [u'2'],
# u'ContactList[34][StarFriend]': [u'0'],

class MemberList(models.Model):
    GroupID = models.TextField()
    AttrStatus = models.TextField()
    DisplayName = models.TextField()
    KeyWord = models.TextField()
    MemberStatus = models.TextField()
    NickName = models.TextField()
    PYInitial = models.TextField()
    PYQuanPin = models.TextField()
    RemarkPYInitial = models.TextField()
    RemarkPYQuanPin = models.TextField()
    Uin = models.TextField()
    UserName = models.TextField()


# UserName]': [u'@431edef0806b5d8b43a16524021898a9'],
# MemberStatus]': [u'0'],
# Uin]': [u'38574705'],
# AttrStatus]': [u'37855335'],
# NickName]': [u'\u674e\u51b0\u6210'],
# RemarkPYQuanPin]': [u''],
# KeyWord]': [u'ice'],
# RemarkPYInitial]': [u''],
# PYInitial]': [u''],
# PYQuanPin]': [u''],
# DisplayName]': [u''],

class UserTalkList(models.Model):
    ToUserName = models.CharField(max_length=40)  # AddMsgList[0][ToUserName]
    FromUserName = models.CharField(max_length=40)  # AddMsgList[0][FromUserName]
    Content = models.TextField()  # AddMsgList[0][Content]
    MsgId = models.TextField()  # AddMsgList[0][MsgId]
    NickName = models.CharField(max_length=30)  # AddMsgList[0][RecommendInfo][NickName]
    SyncKey = models.CharField(max_length=20)  # maybe timestamp SyncKey[List][5][Val]


class GroupTalkList(models.Model):
    ToUserName = models.CharField(max_length=40)  # AddMsgList[0][ToUserName]
    FromUserName = models.CharField(max_length=40)  # AddMsgList[0][FromUserName]
    Content = models.TextField()  # AddMsgList[0][Content]
    MsgId = models.TextField()  # AddMsgList[0][MsgId]
    NickName = models.CharField(max_length=30)  # AddMsgList[0][RecommendInfo][NickName]
    SyncKey = models.CharField(max_length=20)  # maybe timestamp SyncKey[List][5][Val]


class user(models.Model):
    ToUserName = models.CharField(max_length=40)  # AddMsgList[0][ToUserName]
    FromUserName = models.CharField(max_length=40)  # AddMsgList[0][FromUserName]
    Content = models.TextField()  # AddMsgList[0][Content]
    MsgId = models.TextField()  # AddMsgList[0][MsgId]
    NickName = models.CharField(max_length=30)  # AddMsgList[0][RecommendInfo][NickName]
    SyncKey = models.CharField(max_length=20)  # maybe timestamp SyncKey[List][5][Val]

admin.site.register(QRcode)