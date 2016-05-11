 (function(){
        console.log("injected");
        
        chrome.extension.sendMessage({greeting: "hello to extention!"}, function(response) {
            console.log(response.farewell);
        });
    })();
