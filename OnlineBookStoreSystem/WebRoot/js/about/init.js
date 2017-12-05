/**
 * Created by fuookami on 2017/12/1.
 */

jQuery(document).ready(function(){
    $('.button-collapse').sideNav();

    if (jQuery.cookie("curr_login_account")) {
        var objs = jQuery(".log_out_btn");
        objs.show();

        jQuery("#hello_text").html("您好，" + jQuery.cookie("curr_login_account_name"));

        objs.click(function(){
            jQuery.cookie("curr_login_account", null, {expires: -1});

            location.href = "/index";
        });
    } else {
        jQuery(".log_out_btn").hide();
        jQuery("#hello_text").html("您好");
    }
});
