/**
 * Created by fuookami on 2017/12/4.
 */

jQuery(document).ready(function(){
    jQuery('.button-collapse').sideNav();

    jQuery.cookie("curr_search_keywords", null, {expires: -1});
    jQuery.cookie("curr_check_detail_book_uuid", null, {expires: -1});

    if (!jQuery.cookie("curr_login_account")) {
        location.href = "/user_center/login";
    } else {
        jQuery("#hello_text").html("您好，" + jQuery.cookie("curr_login_account_name"));

        jQuery(".log_out_btn").click(function(){
            jQuery.cookie("curr_login_account", null, {expires: -1});

            location.href = "/index";
        });
    }
});
