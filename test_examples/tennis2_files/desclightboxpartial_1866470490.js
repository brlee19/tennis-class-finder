$(function(){$("body").append('<div id="descDivWrapper" class="" style="position:absolute;display:none;z-index:1001;"></div>'),$(".modalBio, .modalClassDesc, .modalLocationInfo").click(function(a){var b="",c=!0,d="",e=$(this);e.hasClass("modalBio")?(b="/Ajax/QuickStaffBio/",d="trnid="+$(this).attr("name").replace("bio","")):e.hasClass("modalClassDesc")?(b="/Ajax/ClassInfo/",d="classid="+$(this).attr("name").replace("cid","")):e.hasClass("modalLocationInfo")?(b="/Ajax/LocationInfo/",d="locid="+$(this).attr("name").replace("loc",""),$("#descDivWrapper").css({width:"auto"})):(b="",d=""),$("#descDivWrapper").html('<div id="removeModal"><img class="LBCloseButton" alt="close" src="/asp/images/close_button.png"/></div><div class="DescDivInfo"><img src="/asp/images/loading-gray-scale_100px.gif" style="display:block;margin-left:auto;margin-right:auto;float:none;"/> </div>');var f=$("#main-content").offset();a.offsetX=a.pageX-f.left,a.offsetY=a.pageY-f.top;var g=a.pageX-$("#descDivWrapper").width()/2,h=a.pageY;a.offsetY>$(window).height()+200?(h=a.pageY-2*$("#descDivWrapper").height()-15,c=!1):(h=a.pageY+20,c=!0),$("#descDivWrapper").css({top:h+"px",left:g+"px"}),$.browser.msie&&-1!=$.browser.version.indexOf("7.0")&&($("#removeModal").css({top:"0px",right:"120px"}),$("#descDivWrapper").css({top:h+"px",left:g+70+"px"})),$("#descDivWrapper").show(),$.ajax({type:"GET",url:b,dataType:"html",data:d,success:function(b){if(null!=b&&""!=b)if(0!=b.indexOf("http:")){$("#descDivWrapper").html('<div id="removeModal" ><img class="LBCloseButton" alt="close" src="/asp/images/close_button.png"/></div>');var d=$('<div class="DescDivInfo" style="xdisplay: none"></div>'),e=$('<div class="DescDivInfoInner" style="xvisibility: hidden"></div>');e.css("opacity",0),$("#descDivWrapper").append(d),d.append(e),d.css("min-height","80px"),e.html(b),e.css("opacity",0).animate({opacity:1},500,function(){$(this).css("opacity","")}),a.offsetY>$(window).height()+800?(h=a.pageY-$("#descDivWrapper").height()-10,c=!1):(h=a.pageY+20,c=!0),$("#descDivWrapper").css({top:h+"px",left:a.pageX-$("#descDivWrapper").width()/2+"px"}),$.browser.msie&&-1!=$.browser.version.indexOf("7.0")&&$("#descDivWrapper").css({top:h+"px",left:a.pageX-$("#descDivWrapper").width()/2+70+"px"}),c?($("#descDivWrapper").append('<div id="triangle" class="triangleUp"></div>'),$("#triangle").css({"margin-left":$("#descDivWrapper").width()/2-6+"px"}),$.browser.msie&&-1!=$.browser.version.indexOf("7.0")&&$("#triangle").css({"margin-left":$("#descDivWrapper").width()/2-80+"px"})):($("#descDivWrapper").append('<span id="triangle" class="triangleDown"></span>'),$("#triangle").css({"margin-top":$("#descDivWrapper").height()-6+"px","margin-left":$("#descDivWrapper").width()/2-6+"px"}),$.browser.msie&&-1!=$.browser.version.indexOf("7.0")&&$("#triangle").css({"margin-top":$("#descDivWrapper").height()-6+"px","margin-left":$("#descDivWrapper").width()/2-80+"px"})),$.browser.msie&&-1!=$.browser.version.indexOf("7.0")&&$("#removeModal").css({top:"0px",right:"120px"})}else window.open(b)}})}),$("#removeModal").live("click",function(){$("#descDivWrapper").html(""),$("#descDivWrapper").hide()})});