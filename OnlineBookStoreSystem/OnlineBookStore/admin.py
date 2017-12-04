from django.contrib import admin

# Register your models here.
from .models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'mail', 'password', 'address', 'balance', 'type', 'trolley')


class UnactivatedAccountAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'mail', 'password', 'address', 'activation_token', 'activation_deadline',
                    'is_activation_finished')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'account', 'content', 'is_sent')


class PaymentOrderAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'account', 'amount', 'creating_time', 'deadline', 'payment_token', 'type', 'content',
                    'is_finished')


class ShoppingOrderAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'account', 'amount', 'content', 'shipping_option', 'payment_order', 'status')


class LogisticsOrderAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'logistics_agent', 'amount', 'shopping_order', 'seller', 'content', 'logistics_token')


class BookAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'author', 'catalog', 'description', 'isbn', 'price', 'image_url')


class UsedBookAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'book', 'seller', 'price', 'server_fee', 'shopping_order', 'description', 'status')


admin.site.register(Account, AccountAdmin)
admin.site.register(UnactivatedAccount, UnactivatedAccountAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(PaymentOrder, PaymentOrderAdmin)
admin.site.register(ShoppingOrder, ShoppingOrderAdmin)
admin.site.register(LogisticsOrder, LogisticsOrderAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(UsedBook, UsedBookAdmin)
