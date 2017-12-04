/**
 * Created by fuookami on 2017/11/28.
 */

jQuery(document).ready(function(){
    $('.button-collapse').sideNav();

    if (jQuery.cookie("curr_search_keywords")) {
        search_books_by_keywords(jQuery.cookie("curr_search_keywords"));

        jQuery.cookie("curr_search_keywords", null);
    }

    jQuery("#search_done").click(function(){
        search_books_by_keywords(jQuery("#search").val());
    });
});

function search_books_by_keywords(keywords) {
    jQuery.ajax({
        type: "POST",
        url: "/book/search_book",
        async: false,
        dataType: "json",
        data: {
            "keywords": keywords
        },
        success: function(data) {
            console.log(data);
        },
        error: function (data) {
            console.log(data);
        }
    })
}
