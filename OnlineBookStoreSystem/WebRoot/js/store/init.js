/**
 * Created by fuookami on 2017/11/28.
 */

jQuery(document).ready(function(){
    $('.button-collapse').sideNav();
    jQuery(".modal").modal();
    jQuery.cookie("curr_check_detail_book_uuid", null, {expires: -1});

    if (jQuery.cookie("curr_login_account")) {
        var objs = jQuery(".log_out_btn");
        objs.show();

        jQuery("#hello_text").html("您好，" + jQuery.cookie("curr_login_account_name"));

        objs.click(function(){
            jQuery.cookie("curr_login_account", null);

            location.href = "/index";
        });
    } else {
        jQuery(".log_out_btn").hide();
        jQuery("#hello_text").html("您好");
    }

    if (jQuery.cookie("curr_search_keywords")) {
        search_books_by_keywords(jQuery.cookie("curr_search_keywords"));

        jQuery("#search").val(jQuery.cookie("curr_search_keywords"));
    }

    jQuery("#search_done").click(function(){
        var search_label = jQuery("#search");
        jQuery.cookie("curr_search_keywords", search_label.val(), {path: "/"});

        search_books_by_keywords(search_label.val());
    });
});

function search_books_by_keywords(keywords) {
    jQuery.ajax({
        type: "POST",
        url: "/book/search_book",
        async: true,
        dataType: "json",
        data: {
            "keywords": keywords
        },
        success: function(data) {
            refresh_books(data.books);
        },
        error: function (data) {
            console.log(data);
        }
    });
}

function refresh_books(data) {
    var new_html = "";

    for (var i = 0, j = data.length; i < j; ++i) {
        new_html += generate_book(data[i]);
    }

    jQuery("#book_container").html(new_html);

    jQuery(".store_check_btn").click(function(){
        jQuery.cookie("curr_check_detail_book_uuid", jQuery(this).attr("uuid"), {path: "/"});

        location.href = "/store/check_book_detail";
    });

    jQuery(".store_add_trolley_btn").click(function(){
        if (!jQuery.cookie("curr_login_account")) {
            jQuery("#warn_login_modal").modal('open');
        }
        else {
            var this_ele = jQuery(this);

            add_trolley(this_ele.attr("uuid"));
        }
    });
}

function generate_book(data) {
    return '<div class="col l3 m4 s6">' +
                '<div class="card hoverable">' +
                    '<div class="card-image waves-effect waves-block waves-light">' +
                        '<img class="activator" src="' + data.image_url + '">' +
                    '</div>' +

                    '<div class="card-content">' +
                        '<span class="card-title activator grey-text text-darken-4 truncate">' + data.title + '</span>' +
                        '<p class="activator"><b>' + data.author + '</b>著<i class="material-icons right">more_vert</i></p>' +
                    '</div>' +

                    '<div class="card-reveal">' +
                        '<span class="card-title grey-text text-darken-4">' + data.title + '<i class="material-icons right">close</i></span>' +
                        '<h5>' + data.author + '著</h5>' +
                        '<p>' + data.description + '</p>' +
                    '</div>' +

                    '<div class="card-action">' +
                        '<span class="left red-text darken-1">$' + data.price + '</span>' +
                        '<a class="right store_check_btn" uuid="' + data.uuid + '" style="margin-right: .25em;"><i class="material-icons right red-text Small">info_outline</i></a>' +
                        '<a class="right store_add_trolley_btn" uuid="' + data.uuid + '"><i class="material-icons right red-text Small">shopping_cart</i></a>' +
                    '</div>' +
                '</div>' +
            '</div>' +
        '</div>';
}

function add_trolley(uuid) {

}
