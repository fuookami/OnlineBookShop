import uuid
import base64

from django.db import models
from django.core.validators import MinValueValidator

from PublicModule import ImageStorage


class Book(models.Model):
    uuid = models.UUIDField(
        auto_created=True,
        default=uuid.uuid1,
        unique=True,
        editable=False,
        verbose_name='uuid'
    )
    title = models.TextField(
        default='',
        verbose_name="标题"
    )
    author = models.TextField(
        default='',
        verbose_name="作者"
    )
    catalog = models.TextField(
        default='',
        verbose_name="目录"
    )
    description = models.TextField(
        default='',
        verbose_name="描述"
    )
    isbn = models.CharField(
        max_length=17,
        default='',
        verbose_name="ISBN"
    )
    price = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ],
        verbose_name="新书价格"
    )
    image_url = models.ImageField(
        upload_to='book_cover',
        storage=ImageStorage.ImageStorage(),
        verbose_name="封面图片"
    )

    class Meta:
        app_label = "OnlineBookStore"
        db_table = "Book"
        managed = True
        verbose_name = "书籍"

    @staticmethod
    def search_by_keywords(keywords):
        objs = Book.objects.all()[0:0]

        for keyword in keywords:
            this_keyword_title_objs = Book.objects.filter(title__contains=keyword)
            this_keyword_author_objs = Book.objects.filter(author__contains=keyword)
            objs = objs | this_keyword_title_objs | this_keyword_author_objs
            objs.distinct()

        if objs.__len__() == 0:
            for keyword in keywords:
                this_keyword_catalog_objs = Book.objects.filter(catalog__contains=keyword)
                this_keyword_description_objs = Book.objects.filter(description__contains=keyword)
                objs = objs | this_keyword_catalog_objs | this_keyword_description_objs
                objs.distinct()

        ret = {
            "books": []
        }

        objs.order_by("-id")
        for obj in objs:
            ret["books"].append({
                "uuid": bytes.decode(base64.b64encode(obj.uuid.bytes)),
                "title": obj.title,
                "author": obj.author,
                "price": obj.price,
                "description": obj.description,
                "image_url": obj.image_url.url
            })

        return ret

    @staticmethod
    def get_by_uuid(_uuid):
        obj = Book.objects.get(uuid=_uuid)
        return obj
