/**
 * Created by fuookami on 2017/12/5.
 */

jQuery(document).ready(function(){
    jQuery('.button-collapse').sideNav();
    jQuery(".modal").modal();

    if (jQuery.cookie("curr_login_account")) {
        location.href = "/user_center";
    }

    jQuery("#login_btn").click(function(){
        login();
    });
});

function login() {
    var account = jQuery("#account").val();
    var password = jQuery("#password").val();

    if (account.length == 0 || password.length == 0) {
        jQuery("#information_box_text").html("账号或密码不能为空");
        jQuery("#information_box").modal("open");
    } else {
        jQuery.ajax({
            type: "POST",
            url: "/account/login",
            async: true,
            dataType: "json",
            data: {
                "mail": jQuery.base64.encode(account),
                "password": jQuery.base64.encode(password)
            },
            success: function(data) {
                get_login_reply(data);
            },
            error: function(data) {
                console.log(data);
            }
        });
    }
}

function get_login_reply(data) {
    if (data.code == 0) {
        jQuery.cookie("curr_login_account", jQuery("#account").val(), {path: "/"});
        jQuery.cookie("curr_login_account_uuid", data.uuid, {path: "/"});
        jQuery.cookie("curr_login_account_name", jQuery.base64.decode(data.name, "utf-8"), {path: "/"});
        jQuery.cookie("curr_login_account_type", data.type, {path: "/"});

        location.href = "/user_center";
    } else if (data.code == 1) {
        jQuery("#information_box_text").html("账号不存在");
        jQuery("#information_box").modal("open");
    } else if (data.code == 2) {
        jQuery("#information_box_text").html("密码错误");
        jQuery("#information_box").modal("open");
    } else if (data.code == 3) {
        jQuery("#information_box_text").html("账号仍未激活");
        jQuery("#information_box").modal("open");
    }
}
