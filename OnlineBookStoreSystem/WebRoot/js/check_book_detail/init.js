/**
 * Created by fuookami on 2017/12/5.
 */

jQuery(document).ready(function(){
    jQuery('.button-collapse').sideNav();
    jQuery(".modal").modal();
    jQuery(".collapsible").collapsible();

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

    if (jQuery.cookie("curr_search_keywords")) {
        jQuery("#search").val(jQuery.cookie("curr_search_keywords"));
    }

    if (!jQuery.cookie("curr_check_detail_book_uuid")) {
        location.href = "/store";
    } else {
        get_book_detail(jQuery.cookie("curr_check_detail_book_uuid"));
    }

    jQuery("#search_done").click(function(){
        jQuery.cookie("curr_search_keywords", jQuery("#search").val(), {path: "/"});

        location.href = "/store";
    });

    jQuery("#add_trolley_btn").click(function(){
        if (!jQuery.cookie("curr_login_account")) {
            jQuery("#warn_login_modal").modal("open");
        } else {
            add_trolley(0, jQuery.cookie("curr_check_detail_book_uuid"));
        }
    });

    jQuery("#register_used_book_btn").click(function(){
        if (!jQuery.cookie("curr_login_account")) {
            jQuery("#warn_login_modal").modal("open");
        }
        else {
            jQuery.cookie("curr_register_used_book_name", jQuery("#title").html(), {path: "/"});

            location.href = "/store/register_used_book";
        }
    });
});

function get_book_detail(uuid) {
    jQuery.ajax({
        type: "POST",
        url: "/book/get_book_detail",
        async: true,
        dataType: "json",
        data: {
            "uuid": uuid
        },
        success: function(data) {
            refresh_book_detail(data);
        },
        error: function (data) {
            console.log(data);
        }
    });
}

function refresh_book_detail(data) {
    console.log(data);

    jQuery("#nav_book_title").html(data.title);
    jQuery("#book_cover").attr("src", data.image_url);
    jQuery("#title").html(data.title);
    jQuery("#author").html(data.author + "著");
    jQuery("#price").html("$" + data.price);
    jQuery("#catalog").html(data.catalog);
    jQuery("#description").html(data.description);

    var new_html = "";
    for (var i = 0, j = data.used_books.length; i < j; ++i) {
        new_html += generate_used_book_detail(data.used_books[i]);
    }
    jQuery("#used_book_container").html(new_html);

    jQuery(".add_used_book_in_trolley_btn").click(function(){
        add_trolley(1, jQuery(this).attr("uuid"));
    });
}

function generate_used_book_detail(data) {
    return '<li>' +
                '<div class="collapsible-header">' +
                    '<span class="red-text" style="margin-right: 2em;">$' + data.price + '</span>' +
                    '<span>出售者：' + data.seller_name + '（' + data.seller_mail + '）</span>' +
                '</div>' +
                '<div class="collapsible-body">' +
                    '<p style="margin-bottom: 2.5em;">' + data.description +
                        '<br><br>' +
                        '<a uuid=' + data.uuid + ' + class="add_used_book_in_trolley_btn waves-effect waves-light btn blue lighten-1 right">将该二手书加入购物车</a>' +
                    '</p>' +
                '</div>' +
            '</li>';
}

function add_trolley(is_used_book, uuid) {

}