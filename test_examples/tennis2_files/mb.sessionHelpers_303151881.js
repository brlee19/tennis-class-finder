window.mb=window.mb||{},window.mb.sessionHelpers={setResetSessionInformation:function(a,b){if("undefined"!=typeof Storage){var c={studioId:a,alertMessage:b};window.sessionStorage.setItem("reset_session_information",JSON.stringify(c))}},getResetSessionInformation:function(){if("undefined"==typeof Storage)return null;var a=window.sessionStorage.getItem("reset_session_information");return JSON.parse(a)},resetSession:function(a,b){if(void 0!==a&&void 0!==b)return alert(b),void(window.location="/ASP/logout.asp?studioid="+a);var c=mb.sessionHelpers.getResetSessionInformation();if(null!=c&&void 0!==c.studioId&&void 0!==c.alertMessage)return alert(c.alertMessage),void(window.location="/ASP/logout.asp?studioid="+c.studioId);var d=window.MB.urlHelper.getUrlParameter("studioid");if(""!==d)return void(window.location="/ASP/logout.asp?studioid="+d);window.location="/launch"}};