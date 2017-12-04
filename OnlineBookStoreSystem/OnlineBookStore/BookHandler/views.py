import base64

from .BookHandlerModule import search_book, get_book_detail
from .UsedBookHandlerModule import get_on_selling_used_book_of_book, get_server_fee, register_used_book
from PublicModule.HTTPResponseDispose import before_send_dispose


def get_search_book_request(request):
    data = request.POST
    return before_send_dispose(search_book(data["keywords"]))


def get_book_detail_request(request):
    data = request.POST
    ret = get_book_detail(data["uuid"])
    ret["used_books"] = get_on_selling_used_book_of_book(data["uuid"])
    return before_send_dispose(ret)


def get_server_fee_request(request):
    data = request.POST
    return before_send_dispose(get_server_fee(data["price"]))


def register_used_book_request(request):
    data = request.POST
    register_ret = register_used_book(
        bytes.decode(base64.b64decode(data["book_uuid"])),
        bytes.decode(base64.b64decode(data["seller_uuid"])),
        data["price"],
        data["description"]
    )

    ret = {
        "code": True if register_ret else False
    }
    return before_send_dispose(ret)
