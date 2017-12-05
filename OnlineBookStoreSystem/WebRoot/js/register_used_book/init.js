/**
 * Created by fuookami on 2017/12/5.
 */

jQuery(document).ready(function(){
    jQuery('.button-collapse').sideNav();
    jQuery('select').not('.disabled').material_select();
    jQuery(".modal").modal();

    if (!jQuery.cookie("curr_check_detail_book_uuid")) {
        location.href = "/store";
    }

    if (!jQuery.cookie("curr_login_account")) {
        location.href = "/user_center/login";
    }

    jQuery("#hello_text").html("您好，" + jQuery.cookie("curr_login_account_name"));
    jQuery("#book_title").html(jQuery.cookie("curr_register_used_book_name"));

    jQuery(".log_out_btn").click(function(){
        jQuery.cookie("curr_login_account", null, {expires: -1});

        location.href = "/index";
    });
});
