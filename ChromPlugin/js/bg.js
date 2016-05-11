(function(){

        var resOK = {
            farewell: "extension send response back..."
        };

        var resError = {
            farewell: "extension hasError!"
        };

        chrome.extension.onMessage.addListener(function(request, sender, sendResponse) {
            console.log("Request comes from content script " + sender.tab.url);

            if (request.greeting === "hello to extention!"){
                sendResponse(resOK);
            }else{
                sendResponse(resError);
            }
        });

    })();