var ticker={position:0,contents:"",init:function(a){window.implementationSwitchIsEnabled("Bug_309353_HeaderGrowsOnIphone5")&&navigator.userAgent.match(/iphone/i)&&$(".floatingHeaderRow").css({height:$(".floatingHeaderRow").height()}),ticker.contents=a||ticker.contents,ticker.next(),ticker.contents.length>1&&setInterval(ticker.next,5e3)},next:function(){var a=ticker.position;$("#memoryticker").fadeOut(500,function(){var b=$(this);b.html(ticker.contents[a]),b.fadeIn(500)}),ticker.position=(a+1)%ticker.contents.length}};