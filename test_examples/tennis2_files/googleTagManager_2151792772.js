window.googleTagManager={getGTMHeaderScript:function(a){var b="(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','"+a+"')",c=document.createElement("script");c.innerHTML=b,document.head.insertBefore(c,document.head.firstElementChild)},getGTMBodyScript:function(a){var b=' \x3c!-- Google Tag Manager (noscript) --\x3e<noscript><iframe src="https://www.googletagmanager.com/ns.html?id="'+a+' height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\x3c!-- End Google Tag Manager (noscript) --\x3e';$("body").append(b)}};