$(document).ready(function(){var a=$("#LoginContent"),b=($("#FacebookConfirmation"),new mb.models.Validate({onfocusout:!1,onkeyup:!1,errorLabelContainer:".js-createAccountValidationError",errorElement:"p",bannerContainer:".js-bannerError:visible",bannerRules:[{element:"#requiredtxtEmail_Address",rules:["remote"]}],messages:{requiredtxtEmail_Address:{required:localization.email}}},localization));a.on("click","#btnNext",function(a){a.preventDefault();var c=$(".LoginPane .js-createAccountRegistrationForm:visible");c.removeData("validator"),b.ValidateForm(c)&&c.submit()}),$("body").off("click.fbNext").on("click.fbNext","#btnFBVerifyLoginNext",function(a){a.preventDefault();var c=$(".LoginPane .js-createAccountRegistrationForm:visible");c.removeData("validator"),b.ValidateForm(c)&&(mbfb.getFBUserInfo(function(){c.find("#requiredtxtEmail_AddressFB:visible").val()}),c.find("#fbid").val(mbfb.getFBID()),c.find("#fbAccessToken").val(mbfb.getFBAccessToken()),c.submit())})});