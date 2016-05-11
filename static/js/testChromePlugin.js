/**
 * Created by liuzheng on 7/14/15.
 */
 chrome.runtime.sendMessage("eomjfpknoknafgheedneaffoomngadhi",{greeting: "hello"}, function(response) {
  console.log(response.farewell);
});
