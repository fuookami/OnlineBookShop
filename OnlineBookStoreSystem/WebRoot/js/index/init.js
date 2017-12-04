/**
 * Created by fuookami on 2017/11/28.
 */

jQuery(document).ready(function(){
    jQuery('.button-collapse').sideNav();
    jQuery('.parallax').parallax();

    jQuery("#search_done").click(function(){
        jQuery.cookie("curr_search_keywords", jQuery("#search").val());

        location.href = "/store";
    });
});
