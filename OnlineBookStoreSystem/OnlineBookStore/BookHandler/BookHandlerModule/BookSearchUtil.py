from ...Models import Book


def search_book(keywords):
    return Book.search_by_keywords(keywords.split(" "))


def get_book_detail(uuid):
    obj = Book.get_by_uuid(uuid)

    return {
        "title": obj.title,
        "author": obj.author,
        "catalog": obj.catalog,
        "description": obj.description,
        "isbn": obj.isbn,
        "price": obj.price,
        "image_url": obj.image_url.url
    }
