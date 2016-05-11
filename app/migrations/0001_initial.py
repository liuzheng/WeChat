# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('WhoseFriend', models.TextField()),
                ('Alias', models.TextField()),
                ('AppAccountFlag', models.TextField()),
                ('AttrStatus', models.TextField()),
                ('ChatRoomId', models.TextField()),
                ('City', models.TextField()),
                ('ContactFlag', models.TextField()),
                ('DisplayName', models.TextField()),
                ('HeadImgUrl', models.TextField()),
                ('HideInputBarFlag', models.TextField()),
                ('KeyWord', models.TextField()),
                ('MemberCount', models.TextField()),
                ('NickName', models.TextField()),
                ('OwnerUin', models.TextField()),
                ('Province', models.TextField()),
                ('PYInitial', models.TextField()),
                ('PYQuanPin', models.TextField()),
                ('RemarkName', models.TextField()),
                ('RemarkPYInitial', models.TextField()),
                ('RemarkPYQuanPin', models.TextField()),
                ('Sex', models.TextField()),
                ('Signature', models.TextField()),
                ('SnsFlag', models.TextField()),
                ('StarFriend', models.TextField()),
                ('Statues', models.TextField()),
                ('Uin', models.TextField()),
                ('UniFriend', models.TextField()),
                ('UserName', models.TextField()),
                ('VerifyFlag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupTalkList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ToUserName', models.CharField(max_length=40)),
                ('FromUserName', models.CharField(max_length=40)),
                ('Content', models.TextField()),
                ('MsgId', models.TextField()),
                ('NickName', models.CharField(max_length=30)),
                ('SyncKey', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LoginUserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UserID', models.TextField()),
                ('UserName', models.TextField()),
                ('UserAvatar', models.TextField()),
                ('UserStatus', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MemberList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('GroupID', models.TextField()),
                ('AttrStatus', models.TextField()),
                ('DisplayName', models.TextField()),
                ('KeyWord', models.TextField()),
                ('MemberStatus', models.TextField()),
                ('NickName', models.TextField()),
                ('PYInitial', models.TextField()),
                ('PYQuanPin', models.TextField()),
                ('RemarkPYInitial', models.TextField()),
                ('RemarkPYQuanPin', models.TextField()),
                ('Uin', models.TextField()),
                ('UserName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QRcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ToUserName', models.CharField(max_length=40)),
                ('FromUserName', models.CharField(max_length=40)),
                ('Content', models.TextField()),
                ('MsgId', models.TextField()),
                ('NickName', models.CharField(max_length=30)),
                ('SyncKey', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserTalkList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ToUserName', models.CharField(max_length=40)),
                ('FromUserName', models.CharField(max_length=40)),
                ('Content', models.TextField()),
                ('MsgId', models.TextField()),
                ('NickName', models.CharField(max_length=30)),
                ('SyncKey', models.CharField(max_length=20)),
            ],
        ),
    ]
