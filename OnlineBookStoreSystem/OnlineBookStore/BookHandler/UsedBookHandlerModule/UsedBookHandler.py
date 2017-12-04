from ...Models import Book, Account, UsedBook


def get_on_selling_used_book_of_book(uuid):
    return UsedBook.get_on_selling_used_book_of_book(uuid)


def get_server_fee(price):
    return {
        "server_fee": UsedBook.get_server_fee(price)
    }


def register_used_book(book_uuid, seller_uuid, _price, _description):
    new_obj = UsedBook(
        book=Book.get_by_uuid(book_uuid),
        seller=Account.get_account_by_uuid(seller_uuid),
        price=_price,
        server_fee=get_server_fee(_price),
        description=_description
    )
    new_obj.save()

    return True
