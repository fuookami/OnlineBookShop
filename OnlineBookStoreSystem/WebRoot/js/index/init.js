/**
 * Created by fuookami on 2017/11/28.
 */

jQuery(document).ready(function(){
    jQuery('.button-collapse').sideNav();
    jQuery('.parallax').parallax();

    jQuery.cookie("curr_search_keywords", null, {expires: -1});
    jQuery.cookie("curr_check_detail_book_uuid", null, {expires: -1});

    jQuery("#search_done").click(function(){
        jQuery.cookie("curr_search_keywords", jQuery("#search").val(), {path: "/"});

        location.href = "/store";
    });

    if (!jQuery.cookie("curr_login_account")) {
        jQuery(".log_out_btn").hide();
        jQuery("#hello_text").html("您好");
    } else {
        var objs = jQuery(".log_out_btn");
        objs.show();

        jQuery("#hello_text").html("您好，" + jQuery.cookie("curr_login_account_name"));

        objs.click(function(){
            jQuery.cookie("curr_login_account", null, {expires: -1});

            location.href = "/index";
        });
    }
});
