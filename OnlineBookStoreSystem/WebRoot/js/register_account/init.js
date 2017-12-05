/**
 * Created by fuookami on 2017/12/5.
 */

jQuery(document).ready(function(){
    jQuery('.button-collapse').sideNav();
    jQuery(".modal").modal();

    if (jQuery.cookie("curr_login_account")) {
        location.href = "/user_center";
    }

    jQuery("#clear_btn").click(function(){
        jQuery("input").val("");
    });

    jQuery("#confirm_btn").click(function(){
        register();
    });
});

function register() {
    var email_input = jQuery("#email");
    var email = email_input.val();
    var email_valid = email_input.hasClass("valid");
    var password = jQuery("#password").val();
    var confirm_password = jQuery("#confirm_password").val();
    var name = jQuery("#name").val();
    var address = jQuery("#address").val();

    if (email.length == 0 || password.length == 0 || confirm_password.length == 0 || name.length == 0
        || address.length == 0) {
        jQuery("#information_box_text").html("任一一个框均不能为空");
        jQuery("#information_box").modal("open");
    } else if (!email_valid) {
        jQuery("#information_box_text").html("邮件地址不合法");
        jQuery("#information_box").modal("open");
    } else if (password !== confirm_password) {
        jQuery("#information_box_text").html("两次输入的密码不相等");
        jQuery("#information_box").modal("open");
    } else if (password.length < 6) {
        jQuery("#information_box_text").html("密码不能短于6个字符");
        jQuery("#information_box").modal("open");
    } else {
        jQuery("#confirm_btn").enabled(false);

        jQuery.ajax({
            type: "POST",
            url: "/account/register",
            async: true,
            dataType: "json",
            data: {
                "mail": jQuery.base64.encode(email),
                "password": jQuery.base64.encode(password),
                "name": jQuery.base64.encode(name, "utf-8"),
                "address": jQuery.base64.encode(address, "utf-8")
            },
            success: function(data) {
                get_register_reply(data);
            },
            error: function(data) {
                console.log(data);
            }
        });
    }
}

function get_register_reply(data) {
    if (data.code == 0) {
        jQuery("#information_box_text").html("注册成功，请前往邮箱查收激活邮件，在" + data.deadline + "前完成激活");
        jQuery("#information_box").modal("open");

        jQuery("#information_box a").click(function(){
            location.href = "/user_center/login";
        });
    } else if (data.code == 1) {
        jQuery("#information_box_text").html("该邮箱地址（账号）已存在");
        jQuery("#information_box").modal("open");
    } else if (data.code == 2) {
        jQuery("#information_box_text").html("不明原因，注册失败");
        jQuery("#information_box").modal("open");
    }

    jQuery("#confirm_btn").enabled(true);
}