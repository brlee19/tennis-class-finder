function ajaxRequest(a,b,c,d){if(objAJAX=!1,window.XMLHttpRequest)objAJAX=new XMLHttpRequest,objAJAX.overrideMimeType&&objAJAX.overrideMimeType("text/xml");else if(window.ActiveXObject)try{objAJAX=new ActiveXObject("Msxml2.XMLHTTP")}catch(a){try{objAJAX=new ActiveXObject("Microsoft.XMLHTTP")}catch(a){}}if(!objAJAX)return alert("Your browser does not support AJAX.  Update your browser or contact MindBody Online."),!1;null==d?(objAJAX.onreadystatechange=c,objAJAX.open("POST",a,!0),objAJAX.setRequestHeader("Content-type","application/x-www-form-urlencoded"),objAJAX.setRequestHeader("Content-length",b.length),objAJAX.setRequestHeader("Connection","close"),objAJAX.send(b)):(objAJAX.open("POST",a,!1),objAJAX.setRequestHeader("Content-type","application/x-www-form-urlencoded"),objAJAX.setRequestHeader("Content-length",b.length),objAJAX.setRequestHeader("Connection","close"),objAJAX.send(b),c())}var objAJAX=!1;