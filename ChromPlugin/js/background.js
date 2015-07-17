chrome.webRequest.onBeforeRequest.addListener(
    function (request) {
        if (localStorage.getItem('isOK') == 'true') {
            var requestUrl = request.url;
            if (requestUrl.match("res.wx.qq.com")) {
                if (requestUrl.match(/.*webwxApp.*js/)) {
                    return {redirectUrl: chrome.extension.getURL('js/webwxApp26cf94.js')};
                    //'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superplus/js/lib/jquery-1.10.2_d88366fd.js'}
                }
                if (requestUrl.match(/.*libs.*js/)) {
                    return {redirectUrl: chrome.extension.getURL('js/libs26cf94.js')};
                    //'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superplus/js/lib/jquery-1.10.2_d88366fd.js'}
                }
                //if(requestUrl.match(/.*libs.*js/)){
                //return {redirectUrl: 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superplus/js/lib/jquery-1.10.2_d88366fd.js'}
                //return {redirectUrl: chrome.extension.getURL('js/libs26cf94.js')}
                //}
            }
            //if (requestUrl.match(/.*testChromePlugin.js/)) {
            //    return {redirectUrl: chrome.extension.getURL('js/testChromePlugin.js')};
            //    //'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superplus/js/lib/jquery-1.10.2_d88366fd.js'}
            //}

            if (requestUrl.match('https://login.weixin.qq.com/qrcode/')) {
                if (!localStorage.getItem(requestUrl)) {
                    //alert(requestUrl);
                    //$.get(requestUrl, function (data) {
                    //    console.log(data);
                    //});
                    //console.log("%c", "line-height:276px;padding:120px;background-size:100% 100%;background:url("+requestUrl+") no-repeat;");
                    for (var i in localStorage) {
                        //clean qrcode avoid overflow
                        if (i.match('https://login.weixin.qq.com/qrcode/')) {
                            localStorage.removeItem(i)
                        }
                    }
                    localStorage.setItem(requestUrl, '1');
                }
            }
            //if (requestUrl.match("/cgi-bin/mmwebwx-bin/webwxsync") && request.method == "POST") {
            //    //console.log(request);
            //    var requestUrl = request.url;
            //    if (Date.parse(new Date()) - localStorage.getItem(requestUrl) > 5000) {
            //        localStorage.setItem(requestUrl, Date.parse(new Date()));
            //        //$.post(requestUrl, function (data) {
            //        //    console.log(data);
            //        //});
            //        //console.log(request.requestBody)
            //    }
            //}
            if (requestUrl.match("/cgi-bin/mmwebwx-bin/webwxgetheadimg")) {
                // group image webwxgetheadimg
                //$.ajax({
                //    type: "GET",
                //    //headers: {"Access-Control-Allow-Origin": "*"},
                //    dataType: 'JSONP',
                //    url: "http://localhost:8000/webwxgetheadimg",
                //    //data: t,
                //    data: {"data":requestUrl},
                //    crossDomain: true,
                //    xhrFields: {
                //        withCredentials: true
                //    }
                //});
            }
            //if (requestUrl.match("/cgi-bin/mmwebwx-bin/webwxgeticon")) {
            //    // friend head image
            //}
        }
    },
    // filters
    {
        urls: ["<all_urls>"]
    },
    // extraInfoSpec
    ["blocking", "requestBody"]
);
//chrome.runtime.onMessage.addListener(function(message,sender,sendResponse){
//    console.log(message);
//  sendResponse({farewell:"goodbye"});
//});
chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
        console.log(sender.tab ?
        "from a content script:" + sender.tab.url :
            "from the extension");
        if (request.greeting == "hello")
            sendResponse({farewell: "goodbye"});
    });
//API_synccheck: 'https://' + pushHost + '/cgi-bin/mmwebwx-bin/synccheck',
//API_webwxdownloadmedia: 'https://' + fileHost + '/cgi-bin/mmwebwx-bin/webwxgetmedia',
//API_webwxuploadmedia: 'https://' + fileHost + '/cgi-bin/mmwebwx-bin/webwxuploadmedia',
//API_webwxpreview: '/cgi-bin/mmwebwx-bin/webwxpreview',
//API_webwxinit: "/cgi-bin/mmwebwx-bin/webwxinit?r="+~new Date(),
//API_webwxgetcontact: "/cgi-bin/mmwebwx-bin/webwxgetcontact",
//API_webwxsync: "/cgi-bin/mmwebwx-bin/webwxsync",
//API_webwxbatchgetcontact: '/cgi-bin/mmwebwx-bin/webwxbatchgetcontact',
//API_webwxgeticon: '/cgi-bin/mmwebwx-bin/webwxgeticon',
//API_webwxsendmsg: '/cgi-bin/mmwebwx-bin/webwxsendmsg',
//API_webwxsendmsgimg: '/cgi-bin/mmwebwx-bin/webwxsendmsgimg',
//API_webwxsendemoticon: '/cgi-bin/mmwebwx-bin/webwxsendemoticon',
//API_webwxsendappmsg: '/cgi-bin/mmwebwx-bin/webwxsendappmsg',
//API_webwxgetheadimg: '/cgi-bin/mmwebwx-bin/webwxgetheadimg',
//API_webwxgetmsgimg: '/cgi-bin/mmwebwx-bin/webwxgetmsgimg',
//API_webwxgetmedia: '/cgi-bin/mmwebwx-bin/webwxgetmedia',
//API_webwxgetvideo: '/cgi-bin/mmwebwx-bin/webwxgetvideo',
//API_webwxlogout: '/cgi-bin/mmwebwx-bin/webwxlogout',
//API_webwxgetvoice: '/cgi-bin/mmwebwx-bin/webwxgetvoice',
//API_webwxupdatechatroom: '/cgi-bin/mmwebwx-bin/webwxupdatechatroom',
//API_webwxcreatechatroom:'/cgi-bin/mmwebwx-bin/webwxcreatechatroom',
//API_webwxstatusnotify: '/cgi-bin/mmwebwx-bin/webwxstatusnotify',
//API_webwxcheckurl: '/cgi-bin/mmwebwx-bin/webwxcheckurl',
//API_webwxverifyuser: '/cgi-bin/mmwebwx-bin/webwxverifyuser',
//API_webwxfeedback: '/cgi-bin/mmwebwx-bin/webwxsendfeedback',
//API_webwxreport: '/cgi-bin/mmwebwx-bin/webwxstatreport',
//API_webwxsearch: '/cgi-bin/mmwebwx-bin/webwxsearchcontact',
//API_webwxoplog: '/cgi-bin/mmwebwx-bin/webwxoplog',